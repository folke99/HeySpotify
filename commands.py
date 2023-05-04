import VoiceRecognizer
from playsound import playsound
from SpotifyApi import SpotifyApi

def activated(recognizer: VoiceRecognizer.VoiceRecognizer):
    text = recognizer.recognize()
    if text:
        if text == "hey spotify" or text == "play spotify" or text == "pay spotify":
            print("RECOGNIZED")
            playsound('activated.wav')
            spotify = SpotifyApi("")  # instantiate SpotifyApi class with access token
            setAction(recognizer, spotify)
            # do something here
        else:
            print("NOT RECOGNIZED")
            print(f"Recognized text: {text}")

def setAction(recognizer: VoiceRecognizer.VoiceRecognizer, spotify: SpotifyApi):
    text = recognizer.recognize()
    if text == "play":
        playsound('activated2.wav')
        song = recognizer.recognize()
        print(song)
        spotify.play_song(song)
    elif text == "stop":
        pass
        spotify.pause()
    elif text == "start":
        spotify.unpause()
    elif text == "next":
        spotify.next_song()
    elif text == "previous":
        spotify.previous_song()