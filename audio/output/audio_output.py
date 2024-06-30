import pyttsx3

class AudioOutput:
    def __init__(self):
        self.engine = pyttsx3.init()

    def falar_resposta(self, resposta):
        print(f"Resposta: {resposta}")
        self.engine.say(resposta)
        self.engine.runAndWait()
