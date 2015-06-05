################################
# NI-DAQ Device as a module :) #
################################
from config import device #from config.py

import os
import ctypes

nidaq = ctypes.windll.nicaiu # load the DLL

""" Setup some typedefs and constants
 to correspond with values in  NIDAQmx.h """
# typedefs
int32 = ctypes.c_long
uInt32 = ctypes.c_ulong
uInt64 = ctypes.c_ulonglong
float64 = ctypes.c_double
TaskHandle = uInt32
# constants
DAQmx_Val_Cfg_Default = int32(-1)
DAQmx_Val_Volts = 10348
DAQmx_Val_Rising = 10280
DAQmx_Val_FiniteSamps = 10178
DAQmx_Val_ContSamps = 10123
DAQmx_Val_GroupByChannel = 0

def CHK(self, err):
    """a simple error checking routine"""
    if err < 0:
        buf_size = 100
        buf = ctypes.create_string_buffer('\000' * buf_size)
        nidaq.DAQmxGetErrorString(err,ctypes.byref(buf),buf_size)
        raise RuntimeError('nidaq call failed with error %d: %s'%(err,repr(buf.value)))
    if err > 0:
        buf_size = 100
        buf = ctypes.create_string_buffer('\000' * buf_size)
        nidaq.DAQmxGetErrorString(err,ctypes.byref(buf),buf_size)
        raise RuntimeError('nidaq generated warning %d: %s'%(err,repr(buf.value)))

def setup(device="dev_device"):
    """Take a name of a device defined in the config file as option."""
    pass

#from ConstantsClass import *
#from CanvasClass import *
print device["name"]
print device["model"]

from matplotlib.pylab import * #refactor - TODO - what for? - also not a great use of import
#from math import pi #refactor - TODO - where? rgrep reveals nothing.

DAQmx_InputSampleRate = float64(1.2e3) #max is float64(1e6), well its 1.25MS/s/channel
DAQmx_OutPutSampleRate = float64(1.2e3) #Its 3.33MS/s
