# python's default config parser
import ConfigParser, os

config = ConfigParser.ConfigParser()
config.readfp(open('device.cfg'))

device_conf = {}
device_conf["name"]=config.get('device', 'name')
print device_conf["name"]
