import anvil.secrets
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
from datetime import datetime
import anvil.files
from anvil.files import data_files
#import anvil.tables as tables
#import anvil.tables.query as q
#from anvil.tables import app_tables
import anvil.server
#code.typing
from typing import List, Tuple, Dict, Set
#data
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from openai import OpenAI
#logging
import logging
import AppLogger

#logger setup
logger = AppLogger.default_server_logging(level=logging.DEBUG)

logger.debug("Server is UP")

def get_uber_data()->pd.DataFrame:
  """
  Reads the Uber raw data CSV file, trims it to 10,000 rows, converts the 'Date/Time' column to datetime,
  and returns the data as a Pandas DataFrame.

  Returns:
      pd.DataFrame: The processed Uber data.
  """
  logger.debug("get_uber_data().read_csv start")
  df = pd.read_csv(data_files['uber-raw-data-sep14.csv'], 
                  nrows=10000)
  df['Date/Time'] = pd.to_datetime(df['Date/Time'])
  logger.debug("get_uber_data().read_csv end")
  return df

@anvil.server.callable
def create_histogram()->np.ndarray:
  """
  Generates a histogram of Uber pick-up counts by hour of the day.

  Returns:
      np.ndarray: Array of counts for each hour: [hour 0 count, hour 1 count, ..., hour 23 count].
  """
  DATA = get_uber_data()
  histogram = np.histogram(DATA['Date/Time'].dt.hour, bins=24)[0] #take values only
  return histogram

@anvil.server.callable
def get_map_data(hour: int = 0)->dict:
  """
  Filters Uber pick-up data for a specific hour and prepares map data.

  Args:
    hour (int): The hour of the day (0-23) to filter data for.

  Returns:
    dict: A dictionary with two keys:
        'map_trace': a Plotly go.Scattermapbox object representing the map markers.
        'pickup_hour_coordinate_pairs': a list of (float, float) tuples representing latitude and longitude pairs.
  """
  logger.debug("get_map_data()(request recieved) start execution")
  DATA = get_uber_data()
  filtered_data = DATA[DATA['Date/Time'].dt.hour == hour]
  logger.debug("get_map_data() end")
  # Plotly trace for the map
  map_data_plot = go.Scattermapbox(lat=filtered_data['Lat'],
                              lon=filtered_data['Lon'],
                              mode = 'markers')
  # Clean coordinate pairs (for AI / analytics)
  coordinate_pairs = list(
    zip(filtered_data['Lat'].tolist(),
        filtered_data['Lon'].tolist())
  )
  logger.debug(f"Coordinate pairs: {coordinate_pairs}")
  return {"hour_map_trace": map_data_plot,
          "pickup_hour_coordinate_pairs": coordinate_pairs}

@anvil.server.callable
def get_ai_response(prompt: str, 
                    pickup_hour: int, 
                    pickup_hour_coordinate_pairs: List[Tuple[float, float]]) -> str:
  """
  Uses OpenAI's API to generate a contextual response based on provided map and demand data.

  Args:
      prompt (str): The user's input prompt.
      pickup_hour (int): The specific hour of the pickup data.
      pickup_hour_coordinate_pairs (list): List of (lat, lon) tuples for pickups.

  Returns:
      str: The AI-generated response content.
  """
  client = OpenAI(api_key=anvil.secrets.get_secret("open_ai_key")) # saved openAI key in the "Secrets" module as "open_ai_key"
  completion = client.chat.completions.create(
    model="gpt-4.1-mini", # Add or adjust the model you want to use here. See "https://platform.openai.com/docs/models" for the model list
  messages=[
      {"role": "system", "content": (
          "You are an expert in urban mobility, ride-hailing logistics, "
          "and Uber driver earnings optimization. You give practical, "
          "location-aware advice based on geographic and hours demand data."
      )},
      {"role": "user", "content": prompt},
      {"role": "user", "content": (
          "Here is relevant map and demand data (list of tuples - pickup coordinates pairs (lat,lon)):\n"
          f"{pickup_hour_coordinate_pairs}\n for a specified hour (24h format): {pickup_hour}"
      )}
  ]
  )
  # Extract the response content
  reply = completion.choices[0].message.content
  logger.debug(f"AI response: {reply}")
  return reply