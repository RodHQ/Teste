import speech_recognition as sr
import sounddevice as sd

class AudioInput:
    def __init__(self, samplerate=44100, duration=5, channels=1):
        self.samplerate = samplerate
        self.duration = duration
        self.channels = channels
        self.recognizer = sr.Recognizer()

    def ouvir_pergunta(self):
        print("Diga algo:")
        recording = sd.rec(int(self.duration * self.samplerate), samplerate=self.samplerate, channels=self.channels, dtype='int16')
        sd.wait()

        audio_data = recording.tobytes()
        try:
            audio = sr.AudioData(audio_data, self.samplerate, 2)
            texto = self.recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {texto}")
            return texto
        except sr.UnknownValueError:
            print("Google Web Speech não conseguiu entender o áudio")
            return None
        except sr.RequestError as e:
            print(f"Erro ao solicitar resultados do serviço Google Web Speech; {e}")
            return None
