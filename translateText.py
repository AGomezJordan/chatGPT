import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(
    api_key = APIKEY
)

def translateText(text, lenguage, model = 'gpt-3.5-turbo'):
    prompt = f"Por favor, traduceme este texto '{text}' al idioma: '{lenguage}'\n El texto traducido al {lenguage} es: "
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
lenguage = input("¿A qué idioma quieres traducirlo?: ")
textTranslated = translateText(text, lenguage)

print('\n--------- Texto traducido -----------\n')
print(textTranslated)