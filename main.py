from GPT.gpt_response import GPTResponse
from audio.input.audio_input import AudioProcessor

def main():
    api_key = 'sua-chave-de-api'
    gpt_response = GPTResponse(api_key)

    # Inicializar a classe de processamento de áudio
    audio_processor = AudioProcessor()
    pergunta = audio_processor.ouvir_e_converter()

    if pergunta:
        resposta = gpt_response.gerar_resposta(pergunta)
        print(resposta)

if __name__ == '__main__':
    main()
