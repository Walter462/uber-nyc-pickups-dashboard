import anvil.secrets
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
from datetime import datetime
import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from typing import List, Tuple, Dict, Set
#data
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from openai import OpenAI
#logging
import logging
import AppLogger

print(f"{datetime.now()} - server UP")

def get_uber_data():
  AppLogger.default_server_logging()
  logger = logging.getLogger('server')
  logger.debug("get_uber_data().read_csv start")
  df = pd.read_csv(data_files['uber-raw-data-sep14.csv'], nrows=10000)
  df['Date/Time'] = pd.to_datetime(df['Date/Time'])
  logger.debug("get_uber_data().read_csv end")
  return df

@anvil.server.callable
def create_histogram():
  DATA = get_uber_data()
  histogram = np.histogram(DATA['Date/Time'].dt.hour, bins=24)[0]
  return histogram

@anvil.server.callable
def get_map_data(hour=0):
  """
  Filter uber pickup data for a specific date and prepare.
  """
  logger = logging.getLogger('server')
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
  print(coordinate_pairs)
  return {"map_trace": map_data_plot,
          "coordinates": coordinate_pairs}

@anvil.server.callable
def get_ai_response(prompt, pickup_hour, pickup_hour_coordinate_pairs): 
  client = OpenAI(api_key=anvil.secrets.get_secret("open_ai_key")) # saved openAI key in the "Secrets" module as "open_ai_key"
  completion = client.chat.completions.create(
    model="gpt-4.1-mini", # Add or adjust the model you want to use here. See "https://platform.openai.com/docs/models" for the model list
    messages=[
      {"role": "system", "content": (
        "You are an expert in urban mobility, ride-hailing logistics, "
        "and Uber driver earnings optimization. You give practical, "
        "location-aware advice based on geographic and hours demand data."
      )},
      {"role": "user","content": (
        "Here is relevant map and demand data (list of tuples - pickup coordinates pairs (lat,lon)):\n"
      f"{pickup_hour_coordinate_pairs}\n for a specified hour (24h format): {pickup_hour}"
      )
      }
    ]
  )
  # Extract the response content
  reply = completion.choices[0].message.content
  print(reply)
  return reply