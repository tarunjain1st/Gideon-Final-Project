import random
from flask import render_template, request, redirect, url_for, session, jsonify, Response
from app import app
from model import *
from helpers.database import *

@app.route('/', methods=["GET"])
def home():
    if "username" in session:
        get_img()
        return render_template('index.html',user=userInfo.find_one({'username':session["username"]})["name"])
    else:
        return render_template('login.html')

# Register new user
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        registerUser()
        return redirect(url_for("login"))

# Check if email already exists in the registratiion page
@app.route('/checkusername', methods=["POST"])
def check():
    return checkusername()

# Everything Login (Routes to renderpage, check if username exist and also verifypassword through Jquery AJAX request)
@app.route('/login', methods=["GET"])
def login():
    if request.method == "GET":
        if "username" not in session:
            return render_template("login.html")
        else:
            return redirect(url_for("home"))


@app.route('/checkloginusername', methods=["POST"])
def checkUserlogin():
    return checkloginusername()


@app.route('/checkloginpassword', methods=["POST"])
def checkUserpassword():
    return checkloginpassword()

# The admin logout
@app.route('/logout', methods=["GET"])  # URL for logout
def logout():  # logout function
    session.pop('username', None)  # remove user session
    return redirect(url_for("home"))  # redirect to home page with message

# Forgot Password
@app.route('/forgot-password', methods=["GET"])
def forgotpassword():
    return render_template('forgot-password.html')

# 404 Page
@app.errorhandler(404)
@app.route('/404', methods=["GET"])
def not_found(e):
    if request.method == "GET":
        if "username" not in session:
            return render_template("404-error.html")
        else:
            return render_template("404.html",user=userInfo.find_one({'username':session["username"]})["name"])


@app.route('/profile', methods=["GET", "POST"])
def profile():
    if request.method == "POST":
        if "username" not in session:
            return render_template("login.html")
        else:
            updateApi()
            return redirect(url_for("home"))
    return render_template("profile.html",user=userInfo.find_one({'username':session["username"]})["name"])


@app.route('/sensorsData', methods=["GET", "POST"])
def checkData():
    return jsonify(sensorsData())


@app.route('/webcam')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
