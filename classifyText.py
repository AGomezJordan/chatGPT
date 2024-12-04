import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(
    api_key = APIKEY
)

def classifyText(text, model = 'gpt-3.5-turbo'):
    categories = [
        'Arte',
        'Ciencia',
        'deportes',
        'economía',
        'educacion'
    ]
    prompt = f"Por favor, clasifica el siguiente texto '{text}' en una de estas categorías: {','.join(categories)}. La categoría es: "
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
textClasiffied = classifyText(text)

print(textClasiffied)