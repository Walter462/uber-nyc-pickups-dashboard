import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
import numpy as np
import plotly.graph_objects as go

def get_uber_data():
  df = pd.read_csv(data_files['uber-raw-data-sep14.csv'], nrows = 10000)
  df['Date/Time'] = pd.to_datetime(df['Date/Time'])
  return df

DATA = get_uber_data()
#print(DATA)
print(anvil.server.get_session_id())
#anvil.server.session["DATA"] = DATA

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
  