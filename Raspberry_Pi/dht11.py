import Adafruit_DHT
DHT_SENSOR=Adafruit_DHT.DHT11
DHT_PIN=4
def getDht():
	hum,temp=Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
	if temp not None:
		return hum,temp
