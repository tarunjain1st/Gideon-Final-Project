import Adafruit_DHT
from pymongo import MongoClient
client=MongoClient("mongodb+srv://test:test@cluster0.glewd.mongodb.net/")
db=client.get_database('demo_db')
record=db.sensor_data
DHT_SENSOR=Adafruit_DHT.DHT11
DHT_PIN=4
while True:
	hum,temp=Adafruit_DHT.read(DHT_SENSOR,DHT_PIN)
	if temp:
		record.update_one({'userId':'helo'},{'$set':{'dht':temp}})
