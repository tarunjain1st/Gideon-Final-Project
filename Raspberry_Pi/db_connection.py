from pymongo import MongoClient
#import win32com.client as win
#speak = win.Dispatch("SAPI.SpVoice")

db_user = ''
db_pass = ''

client = MongoClient("mongodb+srv://{}:{}@cluster0.glewd.mongodb.net/".format(db_user,db_pass))

db = client.get_database('demo_db')
userInfo = db.user_info
sensorData = db.sensor_data
actuatorData = db.actuator_data

class dataLink:
    def __init__(self, api):
        self.api = api
        self.name = ''
        self.userId = ''
        self.userPass = ''

        if dataLink.checkUser(self) == None:
            userInfo.insert_one({'name':self.name,'userId':self.userId,'userPass':self.userPass,'api':self.api})

        '''while len(dataLink.checkUser(self)) == 0:
            count=0
            if count<5000:
                speak.Speak(" Please Update your Profile!")
                speak.Speak(api)
                count=0
            count+1
            '''
        if not sensorData.find_one({'userId':self.userId}):
            sensorData.insert_one({'userId':dataLink.checkUser(self),'temp':0.0,'humidity':0.0,'pir':0,'flame':0,'ldr':0,'mq2':0,'heart':0})
            actuatorData.insert_one({'userId':dataLink.checkUser(self),'motors':{'frontRight':0,'frontLeft':0,'backRight':0,'backLeft':0},'pump':0,'led':0})

    def checkUser(self):
        if(userInfo.find_one({'api':self.api}) == None):
            return None
        self.userId=userInfo.find_one({'api':self.api})['userId']
        return userInfo.find_one({'api':self.api})['userId']

    def uploadDht(self,temp,hum):
        sensorData.update_one({'userId':self.userId},{'$set':{'temp':temp}})
        sensorData.update_one({'userId':self.userId},{'$set':{'humidity':hum}})

    def fetchDht(self):
        return sensorData.find_one({'userId':self.userId})['temp'], sensorData.find_one({'userId':self.userId})['humidity']

    def uploadPir(self,pir):
        sensorData.update_one({'userId':self.userId},{'$set':{'pir':pir}})

    def uploadFlame(self,flame):
        sensorData.update_one({'userId':self.userId},{'$set':{'flame':flame}})

    def uploadMethane(self,mq2):
        sensorData.update_one({'userId':self.userId},{'$set':{'mq2':mq2}})

    def uploadLdr(self,ldr):
        sensorData.update_one({'userId':self.userId},{'$set':{'ldr':ldr}})

    def uploadHeart(self,heart):
        sensorData.update_one({'userId':self.userId},{'$set':{'heart':heart}})

    def fetchMotor(self):
        return actuatorData.find_one({'userId':self.userId})['motors']

    def fetchPump(self):
        return actuatorData.find_one({'userId':self.userId})['pump']

    def fetchLed(self):
        return actuatorData.find_one({'userId':self.userId})['led']
