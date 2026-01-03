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
#data
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from openai import OpenAI
#logging
import logging
import AppLogger
import DataFilters

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
  logger = logging.getLogger('server')
  logger.debug("get_map_data()(request recieved) start execution")
  DATA = get_uber_data()
  filtered_data = DATA[DATA['Date/Time'].dt.hour == hour]
  logger.debug("get_map_data() end")
  
  map_data = go.Scattermapbox(lat=filtered_data['Lat'],
                              lon=filtered_data['Lon'],
                              mode = 'markers')
  return map_data



@anvil.server.callable
def openAI_chat(user_input: str): 
  client = OpenAI(api_key=anvil.secrets.get_secret("open_ai_key")) # Saved openAI key in the `Secrets' module and call it "open_ai_key"
  completion = client.chat.completions.create(
    model="gpt-3.5-turbo-16k", # Add or adjust the model you want to use here. See "https://platform.openai.com/docs/models" for the model list
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": user_input} 
    ],
  )
  # Extract the response content and token count
  agent_response = completion.choices[0].message.content
  print(agent_response)
  return agent_response, token_count