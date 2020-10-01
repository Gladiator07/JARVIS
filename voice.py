import speech_recognition as sr
import pyttsx3

try:
    engine = pyttsx3.init()
except ImportError:
    print('Requested driver not found')
except RuntimeError:
    print('Driver fails to intialize')
voices = engine.getProperty('voices')
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
rate = engine.getProperty('rate')
engine.getProperty('rate', rate)


def speak(response):
    engine.say(response)
    engine.runAndWait()