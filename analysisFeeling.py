import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(
    api_key = APIKEY
)

def analysisFeelling(text, model = 'gpt-3.5-turbo'):
    prompt = f"Por favor, analiza los 3 sentimiento predominantes en el siguiente bloque de comentarios (esta separados por //): '{text}'. El sentimiento es: "
    messages = [
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
        model=model, # Modelo a usar
        messages=messages, # Prompts a mandar
        n=1, # Numero de respuestas
        max_tokens=100, # Maximo de tokens por respuesta
        temperature=0.5
    )

    return response.choices[0].message.content

text = input("Ingresa un texto: ")
feelling = analysisFeelling(text)

print(feelling)