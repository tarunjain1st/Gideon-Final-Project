from friday_functions import *

def prabhoo():
    #engine=engine_init()
    welcome()
    music_flag=False
    player=None
    song=None
    while True:
        query=record().lower()
        if query=="not recorgnized":
            continue;
        print(query)
        if 'prabhu' in query or 'prawhu' in query or 'parabhu' in query or 'pabhu' in query or 'babu' in query:
            if music_flag:
                player.stop()
                os.remove('./temp.'+song.extension)
                music_flag=False
                player=None
                song=None
            playsound("./sound/wake_sound.wav")
            playsound("./sound/wake_sound.wav")
            query=record().lower()
            print(query)
            if 'prabhu' in query or 'prawhu' in query or 'parabhu' in query or 'pabhu' in query:
                if 'bye' not in query and 'goodbye' not in query and 'stop' not in query:
                    playsound("./sound/greeting.wav")
                else:
                    playsound("./sound/thank_you.wav")
                    break

            elif 'bye' in query or 'stop' in query or 'end' in query or 'goodbye' in query:
                playsound("./sound/thank_you.wav")
                break

            elif 'time' in query:
                time=datetime.datetime.now().strftime("%H:%M:%S")
                os.system("echo 'Current time is "+ str(time) +".' | festival --tts")

            elif 'date' in query:
                date=datetime.date.today()
                os.system("echo 'Todays date is " +str(date) +".' | festival --tts")

            elif 'day' in query:
                day=datetime.datetime.now().strftime("%A")
                os.system("echo 'Todays day is "+str(day)+".' | festival --tts")

            elif 'wiki' in query or 'wikipedia' in query or "who is" in query or ('what' in query and 'meaning' not in query and 'temperature' not in query and 'news' not in query and 'affairs' not in query and 'score' not in query):
                search_wikipedia(query)

            elif 'song' in query or 'play' in query or 'music' in query or 'songs' in query or 'musics' in query:
                music_flag,player,song=play_song(query)

            elif 'meaning' in query:
                find_meaning(query)

            elif 'temperature' in query or 'weather' in query or 'climate' in query or 'climatic' in query:
                get_temperature(query)

            elif "cricket" in query or "score" in query or "match" in query:
                get_score(query)

            elif "news" in query or 'affairs' in query:
                get_news()

        else:
            playsound("./sound/error.wav")
            playsound("./sound/error.wav")