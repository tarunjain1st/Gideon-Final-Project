import Adafruit_CharLCD as LCD
from gpiozero import Button
import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
from db_connection import dataLink

remote = dataLink('gideon_v2.0_259634')

GPIO.setmode(GPIO.BCM)

RS = 12
E = 7
D4 = 8
D5 = 24
D6 = 25
D7 = 23
lcd = LCD.Adafruit_CharLCD(RS,E,D4,D5,D6,D7,0,16,2)
count=0
button=Button(14)

while True:
	if count==0:
		lcd.clear()
		lcd.message(datetime.now().strftime('%H:%M:%S')+'\n')
		lcd.message(datetime.now().strftime('%d /%m /%Y'))
	elif count==1:
		lcd.clear()
		lcd.message("Temperature: \n")
        lcd.message(remote.fetchDht())
	elif count==2:
		lcd.clear()
		lcd.message("HeartBeat: \n")
	elif count==3:
		lcd.clear()
		lcd.message("aarjav \n")
	if button.value:
		sleep(0.5)
		print(count)
		count+=1
		if count>3:
			count=0
	sleep(0.1)
