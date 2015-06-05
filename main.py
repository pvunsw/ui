""" This main.py is a guide for the refactor - how we want the python to be once all the cruft is abstracted away. """

import device
import numpy

device.setup("dev_device") #will be stuff in waveform thread

""" TODO: channel will be project specific? - name channels? #auto-return data - do we need side effects extra function calls here? seem un-necessary to me - see def SingleMeasurement(self) in original main."""

point = device.point_measurement(channel, voltage, time)

average = device.average_measurement(channel, voltage, time, total)

""" Maybe this way..."""
with device.measurement(channel, voltage, time) as measurement:
    number = 10
    average = sum([measurement() for i in range(number)])/number
