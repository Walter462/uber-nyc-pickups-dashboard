import anvil.server
import logging
import sys

def basic_anvil_logging():
  logging.basicConfig(level=logging.DEBUG,
                      format='%(asctime)s - %(levelname)s - %(message)s')
  logger = logging.getLogger()
  return logger
