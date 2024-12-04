import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(
    api_key = APIKEY
)

def generate_content(subject, tokens, temperature, model = 'gpt-3.5-turbo'):
    prompt = f"Por favor escribe un artículo corto sobre el tema: {subject}\n\n"
    messages = [
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
        model=model, # Modelo a usar
        messages=messages, # Prompts a mandar
        n=1, # Numero de respuestas
        max_tokens=tokens, # Maximo de tokens por respuesta
        temperature=temperature
    )

    return response.choices[0].message.content

def summary_text(text, tokens, temperature, model = 'gpt-3.5-turbo'):
    prompt = f"Por favor resume el siguiente texto: {subject}\n\n"
    messages = [
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
        model=model, # Modelo a usar
        messages=messages, # Prompts a mandar
        n=1, # Numero de respuestas
        max_tokens=tokens, # Maximo de tokens por respuesta
        temperature=temperature
    )

    return response.choices[0].message.content

subject = input("Elije un tema para tu artículo: ")
tokens = int(input("¿Cuántos tokens máximos tendrá tu artículo: "))
temperature = int(input("Del 1 al 10, ¿Qué tan creativo quieres que sea tu artículo?: ")) / 10

articule = generate_content(subject, tokens, temperature)
print('\n--------------------- Articulo ------------------------------')
print(articule)
print('--------------------- Fin de Articulo ------------------------------\n\n')

tokens = int(input("¿Cuántos tokens máximos tendrá el resumen del artículo generado anteriormente: "))
summary = summary_text(articule, tokens, temperature)
print('\n--------------------- Resumen ------------------------------')
print(summary)
print('\n--------------------- Fin Resumen ------------------------------')