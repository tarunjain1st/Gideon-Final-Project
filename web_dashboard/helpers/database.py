from pymongo import MongoClient
import configuration

connection_params = configuration.connection_params

# connect to mongodb
client = MongoClient(
    "mongodb+srv://{}:{}@cluster0.glewd.mongodb.net/".format('test', 'test'))

db = client.get_database('demo_db')
userInfo = db.user_info
sensorData = db.sensor_data
actuatorData = db.actuator_data
