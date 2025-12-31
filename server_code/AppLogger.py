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
import sys

@anvil.server.callable
def basic_anvil_logging():
  logging.basicConfig(level=logging.DEBUG,
                      format='%(asctime)s - %(levelname)s - %(message)s')
  logger = logging.getLogger()
  return logger

def default_server_logging(logger_name = 'server'):
  logger = logging.getLogger(logger_name)
  handler = logging.StreamHandler(sys.stdout)
  logger.addHandler(handler)
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  handler.setFormatter(formatter)
  logger.setLevel("DEBUG")
  return logger

def data_filter_performance_logging(logger_name='data_filter',
                                    enable=True,
                                    level=logging.DEBUG,
                                    force=True):
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
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
  return logger