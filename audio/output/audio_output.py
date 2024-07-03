import boto3
import os
import pygame
import speech_recognition as sr


def falar_resposta(resposta):
    # Inicializar o cliente do Polly
    polly_client = boto3.Session().client('polly', region_name='sa-east-1')

    # Usar SSML para adicionar pausas e melhorar a entonação
    ssml_text = f"<speak>{resposta}</speak>"

    # Solicitar conversão de texto para fala
    response = polly_client.synthesize_speech(
        TextType='ssml',
        Text=ssml_text,
        OutputFormat='mp3',
        VoiceId='Celine'  # Use 'Camila' para voz em português do Brasil
    )

    # Salvar a resposta de áudio em um arquivo
    with open('resposta.mp3', 'wb') as file:
        file.write(response['AudioStream'].read())

    # Reproduzir o arquivo de áudio
    pygame.mixer.init()
    pygame.mixer.music.load('resposta.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

    # Remover o arquivo de áudio após a reprodução
    os.remove('resposta.mp3')


# Exemplo de uso das funções
if __name__ == "__main__":
    falar_resposta("Bom dia, como vai você?")
else:
    print("Nenhum texto reconhecido.")
