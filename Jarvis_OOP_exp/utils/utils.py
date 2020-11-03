import re
import random
import pyttsx3

class Utils:
    def __init__(self, logger):
        self.logger = logger

    @staticmethod
    def normalize_utterances(utterances):
        normalized = ''
        for u in utterances:
            u = re.sub('\\W+', '',u)
            normalized += u.lower().strip() + "|"
        
        return normalized[:-1]
    
    @staticmethod
    def match_pattern(command, pattern):
        data = Utils.normalize_utterances(pattern)
        compiled = re.compile(data)
        value = compiled.search(command)
        if value:
            return True

        else:
            False

    @staticmethod
    def choose_random(response):
        return random.choice(response)

    @staticmethod
    def speak(response):
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voices', voices[0].id)  

        engine.say(text)
        engine.runAndWait()
        engine.setProperty('rate', 180)
