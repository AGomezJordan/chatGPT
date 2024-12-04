import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(
    api_key = APIKEY
)

lastPrompts = []
lastResponses = []

def ask_chat_gpt(prompt, model = 'gpt-3.5-turbo'):
    messages = [
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
        model=model, # Modelo a usar
        messages=messages, # Prompts a mandar
        n=1, # Numero de respuestas
        max_tokens=150, # Maximo de tokens por respuesta
        temperature=1.5
    )

    return response.choices[0].message.content

print('Bienvenido a nuestro primer chatBOT. Escribe "salir" cuando quieras terminar')
while True:
    conversation = ''
    inpUser = input("\nTu: ")
    if inpUser.lower() == 'salir':
        break
    
    for prompt, response in zip(lastPrompts, lastResponses):
        conversation += f"El usaurio pregunta: {prompt}\n"
        conversation += f"ChatGPT responde: {response}\n"

    prompt = f"El usuario pregunta: {inpUser}\n"
    conversation += prompt
    responseGPT = ask_chat_gpt(conversation)
    print(f"\n{responseGPT}")

    lastPrompts.append(inpUser)
    lastResponses.append(responseGPT)