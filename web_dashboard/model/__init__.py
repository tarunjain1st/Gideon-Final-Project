from app import app
from flask import request, session
from helpers.database import *
from helpers.hashpass import *
from helpers.mailer import *
from bson import json_util, ObjectId
import json
import cv2
import subprocess
import requests

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
    file_id = fs.put(profile_image, filename="username")

    if profile_image and len(api)>0:
        userInfo.update_one({'username': session["username"]}, {'$set': {'api': api,'profile_image_id': file_id}})
    elif len(api)>0:
        userInfo.update_one({'username': session["username"]}, {'$set': {'api': api}})
    elif profile_image:
        userInfo.update_one({'username': session["username"]}, {'$set': {'profile_image_id': file_id}})

def get_img():
    try:
        img_id = userInfo.find_one({'username':session["username"]})["profile_image_id"]
        with open("static/img/avatar.jpg", "wb") as img:
            img.write(fs.get(img_id).read())
    except:
        img_data = requests.get("https://lh3.googleusercontent.com/proxy/jmfpIwPJ-DeCuNmcR0JqYV0f5AqGRzDwxS2X3LFD1y_7nxm6OQl_02dBmJUFnpZWWEMuoqJwBGsTfwegbs8sN4Y9tD6eLGN5GoL4mgA5tDbPqI2W3HfqBbo").content
        with open('static/img/avatar.jpg', 'wb') as handler:
            handler.write(img_data)

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
