import openai

class GPTResponse:
    def __init__(self, api_key):
        openai.api_key = api_key

    def gerar_resposta(self, pergunta):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=pergunta,
            max_tokens=150
        )
        resposta = response.choices[0].text.strip()
        return resposta
