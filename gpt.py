import openai

# Configura la clave de API de OpenAI
openai.api_key = 'TU_CLAVE_DE_API'

# Realiza una solicitud de chat a GPT
response = openai.Completion.create(
    engine='text-davinci-003',
    prompt='Hola, ¿cómo puedo ayudarte hoy?',
    max_tokens=50
)

# Imprime la respuesta de GPT
print(response.choices[0].text.strip())