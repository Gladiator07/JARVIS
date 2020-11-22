import speech_recognition as sr
import os
import pyttsx3
import sys
import json
from Jarvis.features import date_time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

class JarvisAssistant:
    def __init__(self):
        pass
    def mic_input(self):
        """
        Fetch input from mic
        return: user's voice input as text if true, false if fail
        """
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening....")
                r.pause_threshold = 1
                r.adjust_for_ambient_noise(source, duration=1)
                r.energy_threshold = 3000
                audio = r.listen(source)
            try:
                command = r.recognize_google(audio, language='en-in').lower()
                print(f'You said: {command}')
            except:
                print('Please try again')
                command = self.mic_input()
            return command
        except Exception as e:
            print(e)
            return  False


    def tts(self, text):
        """
        Convert any text to speech
        :param text: text(String)
        :return: True/False (Play sound if True otherwise write exception to log and return  False)
        """
        try:
            engine.say(text)
            engine.runAndWait()
            engine.setProperty('rate', 180)
            return True
        except:
            t = "Sorry I couldn't understand and handle this input"
            print(t)
            return False


    def read_json(self):

        with open('Jarvis/config/config.json') as file:
            memory = json.load(file)
        print(memory)
        return memory

    def tell_me_date(self):

        return date_time.date()
