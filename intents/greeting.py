from utils.utils import Utils

class Greeting:
    def __init__(self, logger, response):
        self.logger = logger
        self.response = response

    def speak(self):
        Utils.tts(self.response)