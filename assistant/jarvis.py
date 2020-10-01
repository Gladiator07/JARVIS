import threading
import speech_recognition as sr
class Jarvis:
    def __init__(self, logger, config):
        self.logger = logger
        self.config = config
        self.speech = sr.Recognizer()

    def read_voice(self):
        voice_input = ''
        try:
            with sr.Microphone() as source:
                audio = self.speech.listen(source=source, timeout=5, phrase_time_limit=5)
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

    def run(self):
        while True:
            voice_note = self.read_voice()