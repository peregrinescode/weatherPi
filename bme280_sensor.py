import board
from adafruit_bme280 import basic as adafruit_bme280
from time import sleep

i2c = board.I2C()  # uses board.SCL and board.SDA
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

def read_all():

	humidity  = bme280.humidity
	pressure  = bme280.pressure
	ambient_temperature = bme280.temperature
	
	return humidity, pressure, ambient_temperature
	
