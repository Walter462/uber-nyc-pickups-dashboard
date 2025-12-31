import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import logging
import sys

def basic_anvil_logging():
  logging.basicConfig(level=logging.DEBUG,
                      format='%(asctime)s - %(levelname)s - %(message)s')
  return logging.getLogger()

def data_filter_performance_logging(
  logger_name='data_filter',
  enable=True,
  level=logging.DEBUG,
  force=True
):
  logger = logging.getLogger(logger_name)

  if not enable:
    logger.disabled = True
    return logger

  logger.disabled = False
  logger.setLevel(level)

  if force:
    logger.handlers.clear()

  if not logger.handlers:
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
      '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

  return logger

def get_uber_data():
  #basic_anvil_logging()
  data_filter_performance_logging()
  logger = logging.getLogger('data_filter')
  logger.debug("Custom logger test message")
  #print("Function to log test message")  # Add this line to verify the function is being called
  df = pd.read_csv(data_files['uber-raw-data-sep14.csv'], nrows=10000)
  df['Date/Time'] = pd.to_datetime(df['Date/Time'])
  return df

DATA = get_uber_data()

@anvil.server.callable
def create_histogram():
  histogram = np.histogram(DATA['Date/Time'].dt.hour, bins=24)[0]
  return histogram

@anvil.server.callable
def get_map_data(hour=0):
  filtered_data = DATA[DATA['Date/Time'].dt.hour == hour]
  map_data = go.Scattermapbox(lat=filtered_data['Lat'],
                              lon=filtered_data['Lon'],
                              mode = 'markers')
  return map_data
