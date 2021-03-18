from pymongo import MongoClient
#import win32com.client as win
#speak = win.Dispatch("SAPI.SpVoice")


client = MongoClient("mongodb+srv://test:test@cluster0.glewd.mongodb.net/")
db = client.get_database('demo_db')
userInfo = db.user_info
sensorData = db.sensor_data
actuatorData = db.actuator_data


class dataLink:
    def __init__(self, api):
        self.api = api
        self.username = ""

        while len(dataLink.checkApi(self)) == 0:
            count = 0
            '''if count < 5000:
                speak.Speak(" Please Update your Profile!")
                speak.Speak(api)
                count = 0
            count+1'''

        if not sensorData.find_one({'username': self.username}):
            sensorData.insert_one({'username': dataLink.checkApi(self), 'temperature': 0,'humidity':0, 'pir': 0, 'flame': 0, 'ldr': 0, 'methane': 0, 'heart': 0, 'cpu':0, 'disk':0,'ram':0})
            actuatorData.insert_one({'username': dataLink.checkApi(self), 'pump': 0, 'led': 0, 'buzzer':0})

    def checkApi(self):
        if(userInfo.find_one({'api': self.api}) == None):
            return ""
        self.username = userInfo.find_one({'api': self.api})['username']
        return userInfo.find_one({'api': self.api})['username']

    def updateTemperature(self, temp):
        sensorData.update_one({'username': self.username}, {'$set': {'temperature': temp}})

    def updateHumidity(self, humidity):
        sensorData.update_one({'username': self.username}, {'$set': {'humidity': humidity}})

    def updateDisk(self, disk):
        sensorData.update_one({'username': self.username}, {'$set': {'disk': disk}})

    def updateCpu(self, cpu):
        sensorData.update_one({'username': self.username}, {'$set': {'cpu': cpu}})

    def updateRam(self, ram):
        sensorData.update_one({'username': self.username}, {'$set': {'ram': ram}})

    def updatePir(self, pir):
        sensorData.update_one({'username': self.username}, {'$set': {'pir': pir}})

    def updateFlame(self, flame):
        sensorData.update_one({'username': self.username}, {'$set': {'flame': flame}})

    def updateMethane(self, methane):
        sensorData.update_one({'username': self.username}, {'$set': {'methane': methane}})

    def updateLdr(self, ldr):
        sensorData.update_one({'username': self.username}, {'$set': {'ldr': ldr}})

    def updateHeart(self, heart):
        sensorData.update_one({'username': self.username}, {'$set': {'heart': heart}})

    def updateLed(self, led):
        actuatorData.update_one({'username': self.username}, {'$set': {'led': led}})

    def updatePump(self, pump):
        actuatorData.update_one({'username': self.username}, {'$set': {'pump': pump}})

    def updateBuzzer(self, buzzer):
        actuatorData.update_one({'username': self.username}, {'$set': {'buzzer': buzzer}})



    def fetchPump(self):
        return actuatorData.find_one({'username': self.username})['pump']

    def fetchLed(self):
        return actuatorData.find_one({'username': self.username})['led']

    def fetchBuzzer(self):
        return actuatorData.find_one({'username': self.username})['buzzer']
