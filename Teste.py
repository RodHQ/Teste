from audio.input.audio_input import AudioInput
from audio.output.audio_output import AudioOutput
from GPT.gpt_response import GPTResponse

class Teste:
    def __init__(self, api_key):
        self.audio_input = AudioInput()
        self.audio_output = AudioOutput()
        self.gpt_response = GPTResponse(api_key)

    def executar(self):
        while True:
            pergunta = self.audio_input.ouvir_pergunta()
            if pergunta:
                resposta = self.gpt_response.gerar_resposta(pergunta)
                self.audio_output.falar_resposta(resposta)
