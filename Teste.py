import openai
import speech_recognition as sr
import pyttsx3

class Teste:
    def __init__(self):
        # Inicializar a API GPT
        openai.api_key = 'Teste'  # Substitua pelo seu próprio token da API OpenAI

        # Inicializar o motor de síntese de fala
        self.engine = pyttsx3.init()

    # Função para ouvir a pergunta
    def ouvir_pergunta(self):
        recognizer = sr.Recognizer()
        mic_list = sr.Microphone.list_microphone_names()
        print("Dispositivos de áudio disponíveis:")
        for i, mic_name in enumerate(mic_list):
            print(f"{i}: {mic_name}")

        # Escolher o índice do microfone Logitech USB Headset
        mic_index = mic_list.index("Logitech USB Headset: Audio (hw:1,0)")

        with sr.Microphone(device_index=mic_index) as source:
            print("Diga algo:")
            audio = recognizer.listen(source)
            try:
                pergunta = recognizer.recognize_google(audio, language='pt-BR')
                print(f"Você disse: {pergunta}")
                return pergunta
            except sr.UnknownValueError:
                print("Não consegui entender o que você disse.")
                return None
            except sr.RequestError as e:
                print(f"Erro no serviço de reconhecimento de fala; {e}")
                return None

    # Função para gerar resposta usando a API GPT
    def gerar_resposta(self, pergunta):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": pergunta}
            ]
        )
        resposta = response.choices[0].message['content'].strip()
        return resposta

    # Função para falar a resposta
    def falar_resposta(self, resposta):
        print(f"Resposta: {resposta}")
        self.engine.say(resposta)
        self.engine.runAndWait()

    # Loop principal
    def executar(self):
        while True:
            pergunta = self.ouvir_pergunta()
            if pergunta:
                resposta = self.gerar_resposta(pergunta)
                self.falar_resposta(resposta)