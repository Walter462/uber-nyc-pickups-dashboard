import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import logging
import sys

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