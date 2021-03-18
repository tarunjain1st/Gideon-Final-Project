from flask import Flask, render_template, Response
import cv2
import subprocess

subprocess.Popen("python cam_recv.py")

app = Flask(__name__)
def gen_frames():
    while True:
        frame = cv2.imread('temp.jpg')
        try:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
        except:
            pass
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/webcam')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
