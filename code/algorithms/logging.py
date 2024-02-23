# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 20:38:09 2020

@author: salam_000
"""

import logging

# Create and configure logger

LOG_FORMAT = "%(Levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "E:\\Lumberjack.log", 
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')

logger = logging.getLogger()

# Test messages
logger.debug("This is a harmless debug message.")
logger.info("Just some useful info.")
logger.warning("I'am sorry, but i can't do that, Dave")
logger.error("Did your just try to divide by zero?")
logger.critical("The entire internet is down!")

# Test the logger
#logger.info("Our first message.")
#print(logger.level)