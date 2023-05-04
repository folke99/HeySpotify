import speech_recognition as sr


class VoiceRecognizer:
    def __init__(self):
        self.microphone = sr.Microphone()
        self.recognizer = sr.Recognizer()

    def recognize(self):
        with self.microphone as source:
            print("Speak now...")
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio).strip().lower()
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

        return None
