import threading
import speech_recognition as sr
from utils.utils import Utils
from intents.greeting import Greeting


class Jarvis(threading.Thread):
    def __init__(self, logger, config):
        threading.Thread.__init__(self)

        self.logger = logger
        self.config = config
        self.speech = sr.Recognizer()
        self.utils = Utils(self.logger)

    def read_voice(self):
        voice_input = ''
        try:

            with sr.Microphone() as source:
                self.speech.pause_threshold = 1
                self.speech.energy_threshold = 2000
                self.speech.adjust_for_ambient_noise(source, duration=1)
                self.logger.info('Listening...')

                audio = self.speech.listen(
                    source=source, timeout=5, phrase_time_limit=5)
            voice_input = self.speech.recognize_google(audio)
            self.logger.info(f'You said : {voice_input}')

        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print('Network Error')
        except sr.WaitTimeoutError:
            pass
        except TimeoutError:
            pass
        return voice_input.lower()

    def run(self):
        self.logger.info('Thread is running...')
        session = False
        while True:
            intent = ''
            voice_note = self.read_voice()
            for key in self.config:
                utterances = Utils.match_pattern(voice_note, self.config[key]['utterances'])
                if utterances:
                    intent = key
                    self.logger.info(intent)
                    response = Utils.choose_random(self.config[key]['response'])
                    break

            if intent == 'intent_greeting':
                greeting = Greeting(self.logger, response)
                greeting.speak()
                session = True
                continue
