################################
# NI-DAQ Device as a module :) #
################################
from config import device #from config.py

import os

#from ConstantsClass import *
#from CanvasClass import *
print device["name"]
print device["model"]

from matplotlib.pylab import * #refactor - TODO - what for?
#from math import pi #refactor - TODO - where? rgrep reveals nothing.

DAQmx_InputSampleRate = float64(1.2e3) #max is float64(1e6), well its 1.25MS/s/channel
DAQmx_OutPutSampleRate = float64(1.2e3) #Its 3.33MS/s
