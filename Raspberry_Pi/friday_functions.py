import speech_recognition as sr
#import pyttsx3
import datetime
import wikipedia
import time
from googlesearch import search
from PyDictionary import PyDictionary
import os
from youtubesearchpython import VideosSearch
from youtubesearchpython import PlaylistsSearch
import requests
import json
import vlc
import pafy
import re
from pytube import Playlist
import random
import simpleaudio as sa
from threading import Thread

"""
def engine_init():
    engine=pyttsx3.init()
    engine.setProperty('rate',140)
    engine.setProperty('voice',engine.getProperty('voices')[22].id)
    return engine
    

def text_to_speech(text,engine):
    engine.say(text)
    engine.runAndWait()
"""

def playsound(file_path):
    wave_obj = sa.WaveObject.from_wave_file(file_path)
    play_obj = wave_obj.play()
    play_obj.wait_done()

def welcome():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        playsound("./sound/goodmorning.wav")
    elif hour>=12 and hour<18:
        playsound("./sound/goodafternoon.wav")
    else:
        playsound("./sound/goodevening.wav")

    playsound("./sound/init.wav")

def record():
	r=sr.Recognizer()
	mic=sr.Microphone(device_index = 1)

	with mic as source:
		print("listeninig....")
		r.adjust_for_ambient_noise(source,duration=1)
		audio=r.listen(source)

	try:
		print("recognizing....")
		query=r.recognize_google(audio)

	except Exception:
         playsound("./sound/recorgnising_error.wav")
         return "Not recorgnized"
	return query

def search_wikipedia(query):
    query=query.replace("wikipedia","")
    query=query.replace("wiki","")
    query=query.replace("who is","")
    query=query.replace("what is","")
    try:
        result=wikipedia.summary(query,sentences=1)
        os.system("echo 'according to wikipedia "+ result +" .' | festival --tts")
    except Exception as e:
        playsound("./sound/wikipedia.wav")

def play_song(query):
    query=query.replace('any','')
    query=query.replace('some','')
    query=query.replace('random','')
    query=query.replace('play','')
    if 'songs' in query or 'song' in query or 'music' in query or 'musics' in query:
        playlistsSearch = PlaylistsSearch(query, limit = 2)
        url=str(playlistsSearch.result()['result'][0]['link'])
        playlist = Playlist(url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        url=playlist.video_urls[random.randint(0,len(playlist.video_urls)-1)]
        video=pafy.new(url)
        audiostreams=video.audiostreams
        song=audiostreams[0]
        song.download("temp."+song.extension)
        playsound("./sound/music.wav")
        player = vlc.MediaPlayer("./temp."+song.extension)
        player.play()
        return True,player,song
    else:
        videosSearch = VideosSearch(query, limit=2)
        url=str(videosSearch.result()['result'][0]['link'])
        video=pafy.new(url)
        audiostreams=video.audiostreams
        song=audiostreams[0]
        song.download("temp."+song.extension)
        playsound("./sound/music.wav")
        player = vlc.MediaPlayer("./temp."+song.extension)
        player.play()
        return True,player,song

def find_meaning(query):
    query=query.replace('what','')
    query=query.replace('is','')
    query=query.replace('the','')
    query=query.replace('meaning','')
    query=query.replace('find','')
    query=query.replace('of','')
    query=query.replace('tell me','')
    query=query.replace('search','')
    query=query.replace("word",'')
    query=query.replace('for','')
    query=query.replace('','')
    dictionary=PyDictionary()
    try:
        mean=dictionary.meaning(query)['Noun'][0]
        os.system("echo 'The meaning of the word " +query+ " is "+ mean +" .' | festival --tts")
    except Exception:
        playsound("./sound/meaning.wav")

def get_temperature(query):
    query=query.replace('what','')
    query=query.replace('is','')
    query=query.replace('the','')
    query=query.replace('temperature','')
    query=query.replace('of','')
    query=query.replace('weather','')
    query=query.replace('condition','')
    query=query.replace('in','')
    query=query.replace('climate','')
    query=query.replace('climatic','')
    query=query.replace('condition','')
    query=query.replace('wear','')
    query=query.replace(" ",'')
    link='https://api.openweathermap.org/data/2.5/weather?q={}&appid=5591a568869751699e2473e756d21655'.format(query)
    url=requests.get(link)

    try:
        data=url.json()
        os.system("echo 'Temperature is "+ str(round(data['main']['temp']-273.15,2)) +" . Humidity is "+ str(data['main']['humidity']) +".wind speed is "+ str(data['wind']['speed']) +".' | festival --tts")

    except Exception:
        playsound("./sound/weather.wav")

def get_score(query):
    score=''
    flag=0
    try:
        match_data=requests.get("https://cricapi.com/api/matches?apikey=JABI4051uYhg9z3EI4e7k9UKcT83").json()
        for data in match_data['matches']:
            if datetime.date.today()==datetime.datetime.strptime(data['date'].split('T')[0],'%Y-%m-%d').date() and data['matchStarted']==True:
                score+=requests.get("https://cricapi.com/api/cricketScore?apikey=JABI4051uYhg9z3EI4e7k9UKcT83&unique_id={}".format(data['unique_id'])).json()['score']
                score+='.'
                flag=1
    except Exception:
        playsound("./sound/score.wav")
    if flag==1:
        os.system("echo 'Live Score"+ score +".' | festival --tts")
    else:
        playsound("./sound/nolivematch.wav")

def get_news():
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "32de7139615644cd8c6545d5ef463105"
    }
    main_url = " https://newsapi.org/v1/articles"
    try:
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
    except Exception:
        playsound("./sound/news.wav")
        return None
    article = open_bbc_page["articles"]
    playsound("./sound/top_headline.wav")
    os.system("echo "+ article[0]['title'] +" | festival --tts")
