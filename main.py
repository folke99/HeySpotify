import AuthTokenRequest
import VoiceRecognizer
import commands

if __name__ == "__main__":
    recognizer = VoiceRecognizer.VoiceRecognizer()
    while True:
        commands.activated(recognizer)