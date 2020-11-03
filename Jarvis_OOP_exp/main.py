import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening:")
        r.pause_threshold = 1
        r.energy_threshold = 3000
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        command = ''

        try:
            print("Recognizing")
            command = r.recognize_google(audio, language='en-in')

            print(f"You said: {command}\n")

        except Exception as e:
            print("Exception: " + str(e))

        return command


def speak(text):
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 180)

speak(get_audio())