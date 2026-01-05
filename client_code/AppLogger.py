import anvil.facebook.auth
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.server
import logging
import sys

def basic_anvil_logging():
  """
  Enable for disable basic logging.
  level=logging.DEBUG,
  format='%(asctime)s - %(levelname)s - %(message)s'
  """
  logging.basicConfig(level=logging.DEBUG,
                      format='%(asctime)s - %(levelname)s - %(message)s')
  logger = logging.getLogger()
  return logger

def default_server_logging(logger_name = 'server',
                          level=logging.DEBUG):
  """
  Enable or disable logging for a specific logger.

  Parameters
  ----------
  logger_name : str, optional
      Name of the logger to configure. 
      Default: "server"
  enable : bool, optional
      If True, enable the logger; if False, disable it.
  level : int, optional
      Logging level to set when enabling the logger.
      Common levels include:
      - logging.DEBUG     10
      - logging.INFO      20
      - logging.WARNING   30
      - logging.ERROR     40
      - logging.CRITICAL  50
      Default: logging.DEBUG
    Returns
    -------
      None
    """
  logger = logging.getLogger(logger_name)
  handler = logging.StreamHandler(sys.stdout)
  logger.addHandler(handler)
  formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
  handler.setFormatter(formatter)
  logger.setLevel(level)
  return logger


"""
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
"""