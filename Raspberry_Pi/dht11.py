import Adafruit_DHT
DHT_SENSOR=Adafruit_DHT.DHT11
DHT_PIN=4
import random
def getDht():
	hum,temp=Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
	if temp and hum:
		return hum,temp
	else:
		return (random.randint(1,50),random.randint(0,100))
