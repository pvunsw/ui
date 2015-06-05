""" This main.py is a guide for the refactor - how we want the python to be once all the cruft is abstracted away. """

import device
import numpy

device.setup("dev_device") #will be stuff in waveform thread

""" TODO: channel will be project specific? - name channels? #auto-return data - do we need side effects extra function calls here? seem un-necessary to me - see def SingleMeasurement(self) in original main."""

data = device.point_measurement(channel, voltage, time)

average = device.average_measurement(channel, voltage, time, total)

#with device.measurement(channel, voltage, time) as point_measurement:
#    average =
