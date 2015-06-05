import ConfigParser, os

config = ConfigParser.ConfigParser()
config.readfp(open('../device.cfg'))

# TODO - what if not dev device etc.
device = {}
device["name"]=config.get('device', 'name')
device["model"]=config.get('device', 'model')
device["input_samplerate"]=config.get('device', 'input_samplerate')
device["output_samplerate"]=config.get('device', 'output_samplerate')
