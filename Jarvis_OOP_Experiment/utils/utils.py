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

    def speak(self, response):
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voices', self.voices[0].id)
        self.engine.say(response)
        self.engine.runAndWait()
