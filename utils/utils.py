import re

class Utils:
    def __init__(self, logger):
        self.logger = logger
    
    def normalize_utterances(self, utterances):
        for u in utterances:
            u = re.sub('\\W+','',u)
            normalized += u.lower().strip()+"|"

        return normalized[:-1]