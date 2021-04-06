from app import app
from flask import request, session
from helpers.database import *
from helpers.hashpass import *
from helpers.mailer import *
from bson import json_util, ObjectId
import json
import cv2
import subprocess

subprocess.Popen("python cam_recv.py")


def checkloginusername():
    username = request.form["username"]
    check = userInfo.find_one({"username": username})
    if check is None:
        return "No User"
    else:
        return "User exists"


def checkloginpassword():
    username = request.form["username"]
    check = userInfo.find_one({"username": username})
    password = request.form["password"]
    hashpassword = getHashed(password)
    if hashpassword == check["password"]:
        session["username"] = username
        return "correct"
    else:
        return "wrong"


def checkusername():
    username = request.form["username"]
    check = userInfo.find_one({"username": username})
    if check is None:
        return "Available"
    else:
        return "Username taken"


def registerUser():
    fields = [k for k in request.form]
    values = [request.form[k] for k in request.form]
    data = dict(zip(fields, values))
    user_data = json.loads(json_util.dumps(data))
    user_data["password"] = getHashed(user_data["password"])
    user_data["confirmpassword"] = getHashed(user_data["confirmpassword"])
    user_data['api'] = ''
    userInfo.insert(user_data)
    sendmail(subject="Registration Confirmation – Gideon Desk", sender="Gideon Supports Desk",
             recipient=user_data["email"], body="You successfully registered on Gideon Dashboard", name=user_data["name"])
    print("Done")


def sensorsData():
    try:
        data = sensorData.find_one({'username': session["username"]})
        data.pop("_id")
        return data
    except:
        return "null"


def updateApi():
    api = request.form["api"]
    profile_image = request.files["profile_image"]
    if profile_image:
        file_id = fs.put(profile_image, filename="username")
        userInfo.update_one({'username': session["username"]}, {'$set': {'api': api,'profile_image_id': file_id}})
        ''''with open("test.jpg", "wb") as img:
            img.write(fs.get(userInfo.find_one({'username':session["username"]})["profile_image_id"]).read())
'''


def gen_frames():
    while True:
        pass
        frame = cv2.imread('temp.jpg')
        try:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
        except:
            pass
