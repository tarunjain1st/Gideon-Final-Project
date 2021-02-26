from db_connection import dataLink
from threading import Thread
from webcam import streamVideo

api='gideon_v2.0_259634'

if __name__ == "__main__":
    Thread(target = streamVideo).start()
