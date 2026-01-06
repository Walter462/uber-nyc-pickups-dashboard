from ._anvil_designer import Form1Template
from anvil import *
import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import plotly.graph_objects as go
#import anvil.tables as tables
#import anvil.tables.query as q
#from anvil.tables import app_tables
import m3.components as m3
#data
from datetime import datetime
import plotly.graph_objects as go
#logging
import logging
from .. import AppLogger

logger = AppLogger.basic_anvil_logging() #set frontend logger

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    anvil.users.login_with_form()
    self.init_components(**properties)
    self.pickup_hour: int = None
    self.pickup_hour_coordinate_pairs: list = None
    # Plots
    Plot.templates.default = 'rally'
    # Histogram on uber pickup per hour
    self.bar_chart.data = go.Bar(y=anvil.server.call('create_histogram'))
    # MAP
    # Initialise the dropdown and map
    self.hour_dropdown.items =[(f'{n}:00', n) for n in range(0,24)]
    self.hour_dropdown.selected_value = 0
    self.hour_dropdown_change() #plot default 0-hour map
    self.mapbox_map.layout.mapbox = dict(
      style="carto-positron", #[open-street-map, carto-positron, carto-darkmatter, white-bg]
      center = dict(lat=40.7128, lon=-74.0060), 
      zoom=10)
    self.mapbox_map.layout.margin = dict(t=0, b=0, l=0, r=0)
    
  @handle("hour_dropdown", "change")
  def hour_dropdown_change(self, **event_args):
    pickup_hour = self.hour_dropdown.selected_value
    self.pickup_hour = pickup_hour
    self.mapbox_title.text = f'Number of pickups at {pickup_hour}:00'
    logger.debug("Fetching map data: send get_map_data() server request")
    hour_map_data = anvil.server.call('get_map_data', pickup_hour)
    self.mapbox_map.data = hour_map_data['hour_map_trace']
    self.pickup_hour_coordinate_pairs = hour_map_data['pickup_hour_coordinate_pairs']
    logger.debug("End pickup hour map drawing")

  @handle("submit_api", "click")
  def submit_api_click(self, **event_args):
    """This method is called when the component is clicked."""
    self.response.text=""
    self.response.height=58
    prompt = self.prompt.text
    response = anvil.server.call('get_ai_response', 
                                prompt = prompt, 
                                pickup_hour = self.pickup_hour,
                                pickup_hour_coordinate_pairs = self.pickup_hour_coordinate_pairs,
                                output = 'json')
    self.response.text = response

  @handle("submit_txt", "click")
  def submit_txt_click(self, **event_args):
    """This method is called when the component is clicked."""
    self.response.text=""
    self.response.height=58
    prompt = self.prompt.text
    response = anvil.server.call('get_ai_response', 
                                prompt = prompt, 
                                pickup_hour = self.pickup_hour,
                                pickup_hour_coordinate_pairs = self.pickup_hour_coordinate_pairs,
                                output = 'txt')
    self.response.text = response
