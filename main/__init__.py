import speech_recognition as sr
import os
import pyttsx3
import sys

import features.date_time as dt

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

class Jarvis:
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
                command = self.mic_input)
            return command
        except Exception as e:
            print(e)
            return  False


        def speak(self, text):
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


