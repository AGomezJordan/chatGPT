import os, json, spacy
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(
    api_key = APIKEY
)

model = "gpt-3.5-turbo"
prompt = "Cuenta una historia breve sobre un viaje a europa."
messages = [
    {"role": "user", "content": prompt}
]

response = client.chat.completions.create(
    model=model, # Modelo a usar
    messages=messages, # Prompts a mandar
    n=1, # Numero de respuestas
    max_tokens=100 # Maximo de tokens por respuesta
)

print(response)
print()

textGenerated = response.choices[0].message.content

print(textGenerated)

print('\n----------------------------------\n')

modelSpacy = spacy.load("es_core_news_md")
analysis = modelSpacy(textGenerated)

location = None

for entity in analysis.ents:
    if entity.label_ == 'LOC':
        location = entity
        break

if location:
    prompt2 = f"Dime más acerca de {location}"
    messages2 = [
        {"role": "user", "content": prompt2}
    ]

    response2 = client.chat.completions.create(
        model=model, # Modelo a usar
        messages=messages2, # Prompts a mandar
        n=1, # Numero de respuestas
        max_tokens=100 # Maximo de tokens por respuesta
    )
    textGenerated = response2.choices[0].message.content
    print(textGenerated)