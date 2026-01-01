from datetime import datetime
import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
import numpy as np
import plotly.graph_objects as go
#logging
import logging
import AppLogger
from .. import DataFilters

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
