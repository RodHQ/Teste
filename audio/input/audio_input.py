import speech_recognition as sr

class AudioInput:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def ouvir_pergunta(self):
        with sr.Microphone() as source:
            print("Diga algo:")
            audio = self.recognizer.listen(source)
            try:
                pergunta = self.recognizer.recognize_google(audio, language='pt-BR')
                print(f"Você disse: {pergunta}")
                return pergunta
            except sr.UnknownValueError:
                print("Não consegui entender o que você disse.")
                return None
            except sr.RequestError as e:
                print(f"Erro no serviço de reconhecimento de fala; {e}")
                return None
