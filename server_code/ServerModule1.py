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

def basic_anvil_logging():
  logging.basicConfig(level=logging.DEBUG, 
                      format='%(asctime)s - %(levelname)s - %(message)s')
  return logging.getLogger()

def data_filter_perfomance_logging(logger_name = 'data_filter',
                                  enable = True,
                                  level = logging.DEBUG):
  logger = logging.getLogger(logger_name)
  if enable:
    logger.setLevel(level)
    if not logger.handlers:
      console = logging.StreamHandler()
      formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
      console.setFormatter(formatter)
      logger.addHandler(console)
    else:
      logger.disabled = True
  
def get_uber_data():
  basic_anvil_logging()
  data_filter_perfomance_logging()
  logging.getLogger('data_filter').debug("Logger test message")
  df = pd.read_csv(data_files['uber-raw-data-sep14.csv'], nrows = 10000)
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
  