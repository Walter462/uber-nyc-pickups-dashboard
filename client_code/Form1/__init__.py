from ._anvil_designer import Form1Template
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import m3.components as m3
#data
from datetime import datetime
import plotly.graph_objects as go
#logging
import logging
from .. import AppLogger

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    anvil.users.login_with_form()
    self.init_components(**properties)
    Plot.templates.default = 'rally'
    # Histogram on uber pickup per hour
    self.bar_chart.data = go.Bar(y=anvil.server.call('create_histogram'))

    # Initialise the dropdown and map
    self.hour_dropdown.items =[(f'{n}:00', n) for n in range(0,24)]
    self.hour_dropdown.selected_value = 0
    #self.mapbox_map.data = anvil.server.call('get_map_data')
    self.hour_dropdown_change()
    
    self.mapbox_map.layout.mapbox = dict(
      style="carto-positron", #[open-street-map, carto-positron, carto-darkmatter, white-bg]
      center = dict(lat=40.7128, lon=-74.0060), 
      zoom=10)
    self.mapbox_map.layout.margin = dict(t=0, b=0, l=0, r=0)

  @handle("hour_dropdown", "change")
  def hour_dropdown_change(self, **event_args):
    logger = AppLogger.basic_anvil_logging()
    logger.debug("Start")
    time = self.hour_dropdown.selected_value
    self.mapbox_title.text = f'Number of pickups at {time}:00'
    logger.debug("Fetching map data")
    logger.debug("Send get_map_data() server request")
    self.mapbox_map.data = anvil.server.call('get_map_data', time)
    trace = self.mapbox_map.data[0]
    lats = trace.lat
    lons = trace.lon
    coordinates = list(zip(lats, lons))
    print(coordinates) 
    logger.debug("End")

  @handle("submit", "click")
  def submit_click(self, **event_args):
    """This method is called when the component is clicked."""
    prompt = self.prompt.text
    map_data = self.mapbox_map.data
    response = anvil.server.call('getresponse', prompt)
    self.response.text = response
    pass
