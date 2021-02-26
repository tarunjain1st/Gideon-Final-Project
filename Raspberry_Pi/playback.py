import vlc
import pafy
url = "https://youtu.be/ajtGlNRsM-I"

video = pafy.new(url)

audiostreams = video.audiostreams
for a in audiostreams:
    print(a.bitrate, a.extension, a.get_filesize())
song=audiostreams[0]
print(song)

song.download("temp."+song.extension)

player = vlc.MediaPlayer("./temp.webm")
while True:
    a=input("1.Play \n2.Pause \n3.Stop \n Enter Choice :")
    if a=='1':
        player.play()

    if a=='2':
        player.pause()

    if a=='3':
        player.stop()
