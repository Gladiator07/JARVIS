import re
import random
import os


class Utils:
    def __init__(self, logger):
        self.logger = logger

    @staticmethod
    def normalize_utterances(self, utterances):
        for u in utterances:
            u = re.sub('\\W+', '', u)
            normalized += u.lower().strip()+"|"

        return normalized[:-1]

    @staticmethod
    def match_pattern(voice_note, pattern):
        data = Utils.normalize_utterances(pattern)
        compiled = re.compile(data)
        value = compiled.search(voice_note)
        if value:
            return True
        else:
            False

    @staticmethod
    def choose_random(response):
        return random.choice(response)

    @staticmethod
    def tts(response):
        os.system('say {}'.format(response))
