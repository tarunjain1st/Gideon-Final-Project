from db_connection import dataLink
from threading import Thread
from webcam import streamVideo
#from arduino_com import arudino_cam, arudino_data
from voice_module import prabhoo
from dht11 import getDht
import psutil,time
api='gideon_v2.0_259634'

db = dataLink(api)

def upLink():
    while True:
        dht = getDht()
        hum = dht[0]
        temp = dht[1]
        cpu = psutil.cpu_percent()
        r_memory = psutil.virtual_memory()
        ram = round(r_memory.available/1024.0/1024.0,1)
        d_memory = psutil.disk_usage('/')
        disk = round(d_memory.free/1024.0/1024.0/1024.0,1)

        if temp != 0:
            db.updateHumidity(hum)
            db.updateTemperature(temp)
        db.updateCpu(cpu)
        db.updateRam(ram)
        db.updateDisk(disk)
'''        meth = arudino_data()
        print(meth)
        if meth != 0:
            db.updateMethane(arudino_data())
'''
if __name__ == "__main__":
    Thread(target = streamVideo).start()
    #Thread(target = arudino_cam).start()
    Thread(target = upLink).start()
    Thread(target = prabhoo).start()
