from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import plotly.graph_objects as go
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import m3.components as m3
#import logging

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
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
    logger = anvil.server.call()
    logger.debug("Start")
    time = self.hour_dropdown.selected_value
    self.mapbox_title.text = f'Number of pickups at {time}:00'
    with anvil.server.no_loading_indicator:
      self.mapbox_map.data = anvil.server.call('get_map_data', time)
    logger.info("End")