import openai

class GPTResponse:
    def __init__(self, api_key):
        openai.api_key = api_key

    def gerar_resposta(self, pergunta):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": pergunta}
            ]
        )
        resposta = response['choices'][0]['message']['content'].strip()
        return resposta
