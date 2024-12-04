import os, spacy
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(
    api_key = APIKEY
)

lastPrompts = []
lastResponses = []
modelSpacy = spacy.load("es_core_news_md")

wordsNotAllowed = ["coca-cola", 'pepsi', 'fanta']

def fitlerWord(text, blackList):
    tokens = modelSpacy(text)
    result = []

    for t in tokens:
        if t.text.lower() not in blackList:
            result.append(t.text)
        else:
            result.append('[NOT_ALLOWED]')
    return ' '.join(result)

def ask_chat_gpt(prompt, model = 'gpt-3.5-turbo'):
    messages = [
        {"role": "user", "content": prompt},
    ]

    response = client.chat.completions.create(
        model=model, # Modelo a usar
        messages=messages, # Prompts a mandar
        n=1, # Numero de respuestas
        max_tokens=50, # Maximo de tokens por respuesta
        temperature=0.5
    )

    responseNotFiltered = response.choices[0].message.content
    responseFilteres = fitlerWord(responseNotFiltered, wordsNotAllowed)
    return responseFilteres

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