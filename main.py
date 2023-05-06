import AuthTokenRequest
import VoiceRecognizer
import commands
import auth

if __name__ == "__main__":
    recognizer = VoiceRecognizer.VoiceRecognizer()
    auth.start_token_refresh_loop()
    while True:
        commands.activated(recognizer)