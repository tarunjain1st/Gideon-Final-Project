from db_connection import dataLink
from threading import Thread
from webcam import streamVideo
from dht11 import getDht
import psutil,time
api='gideon_v2.0_259634'

db = dataLink(api)

def upLink():
    while True:
        dht = getDht()
        print(dht['temp'])
        print(dht['hum'])

        #hum,temp = getDht()
        cpu = psutil.cpu_percent()
        r_memory = psutil.virtual_memory()
        ram = round(r_memory.available/1024.0/1024.0,1)
        d_memory = psutil.disk_usage('/')
        disk = round(d_memory.free/1024.0/1024.0/1024.0,1)


        db.updateHumidity(hum)
        db.updateTemperature(temp)
        db.updateCpu(cpu)
        db.updateRam(ram)
        db.updateDisk(disk)

        time.sleep(1)


if __name__ == "__main__":
    #Thread(target = streamVideo).start()
    Thread(target = upLink).start()
