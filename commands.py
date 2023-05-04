import VoiceRecognizer
from playsound import playsound
from SpotifyApi import SpotifyApi

def activated(recognizer: VoiceRecognizer.VoiceRecognizer):
    text = recognizer.recognize()
    if text:
        if text == "hey spotify" or text == "play spotify" or text == "pay spotify":
            print("RECOGNIZED")
            playsound('activated.wav')
            spotify = SpotifyApi("BQAbf6mb-i6p1cGV1Ut-sGMYydWN3QfX5hjV07ZyZWoszQCRTqI4OG_Ct0kms_-jlDJ-oslqHPRNW9O2pu8_z8bWtUMmhIYM7BlHX0YmLL1NbIHvbrpwjf8beOM1P28njikrW5WiUHz-5yq9JNRPZgnMGiwN5wNCvCmb_upXNOeTxwdKexL9lW0WsfmjHl1gcmDDOLsHPb9qsbJA3Y8q3dGt2Jhy11KbF423")  # instantiate SpotifyApi class
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