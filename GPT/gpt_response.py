import openai

class GPTResponse:
    def __init__(self, api_key):
        openai.api_key = api_key

    def gerar_resposta(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente útil."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message['content']

# Exemplo de uso da classe GPTResponse
if __name__ == "__main__":
    api_key = 'sua-chave-de-api'
    gpt_response = GPTResponse(api_key)
    resposta = gpt_response.gerar_resposta("Olá, como você está?")
    print(resposta)
