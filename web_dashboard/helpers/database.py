from pymongo import MongoClient
import gridfs
import configuration

connection_params = configuration.connection_params

# connect to mongodb
client = MongoClient("")    #address

db = client.get_database('demo_db')
fs = gridfs.GridFS(db)
userInfo = db.user_info
sensorData = db.sensor_data
actuatorData = db.actuator_data
