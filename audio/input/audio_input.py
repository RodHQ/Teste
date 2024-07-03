import speech_recognition as sr
import sounddevice as sd


class AudioInput:


    def ouvir_e_converter(self):
        # Configurações de áudio
        samplerate = 44100  # Taxa de amostragem
        duration = 5  # Duração em segundos
        channels = 1  # Mono

        # Captura o áudio
        print("Diga algo:")
        recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16')
        sd.wait()  # Espera a gravação terminar

        # Converte o áudio capturado em bytes
        audio_data = recording.tobytes()

        # Usa speech_recognition para converter áudio em texto
        recognizer = sr.Recognizer()
        try:
            # Usa recognizer para reconhecer o áudio
            audio = sr.AudioData(audio_data, samplerate, 2)
            texto = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Você disse: {texto}")
            return texto
        except sr.UnknownValueError:
            print("Google Web Speech não conseguiu entender o áudio")
            return None
        except sr.RequestError as e:
            print(f"Erro ao solicitar resultados do serviço Google Web Speech; {e}")
            return None
