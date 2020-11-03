from utils.utils import Utils

class Greeting:
    def __init__(self, logger, response):
        self.logger = logger
        self.response = response
        self.utils = Utils(self.logger)

    def speak(self):
        self.utils.speak(self.response)