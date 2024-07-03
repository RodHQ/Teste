import speech_recognition as sr

from audio.output.audio_output import falar_resposta


def ouvir_e_converter():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo:")
        # Ajusta o reconhecimento de energia para a fonte de áudio atual (microfone)
        recognizer.adjust_for_ambient_noise(source, duration=1)
        # Listen for the first phrase and extract it into audio data
        audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)

    try:
        texto = recognizer.recognize_google(audio, language='pt-BR')
        print(f"Você disse: {texto}")
        return texto
    except sr.UnknownValueError:
        print("Google Web Speech não conseguiu entender o áudio")
        return None
    except sr.RequestError as e:
        print(f"Erro ao solicitar resultados do serviço Google Web Speech; {e}")
        return None

# Exemplo de uso da função ouvir_e_converter
if __name__ == "__main__":
    texto = ouvir_e_converter()
    if texto:
        falar_resposta(texto)
        print(f"Texto reconhecido: {texto}")
    else:
        print("Nenhum texto reconhecido.")
