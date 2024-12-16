import os, spacy, numpy
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

def similitudCoseno(vec1, vec2):
    superposicion = numpy.dot(vec1, vec2)
    magnitud1 = numpy.linalg.norm(vec1)
    magnitud2 = numpy.linalg.norm(vec2)

    return superposicion / (magnitud1 * magnitud2)

def isRelevant(response, inputText, umbral = 0.5):
    inputVectoriced = modelSpacy(inputText).vector
    responseVectoriced = modelSpacy(response).vector
    similitud = similitudCoseno(inputVectoriced, responseVectoriced)

    return similitud >= umbral

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
        model=model,
        messages=messages,
        n=1,
        max_tokens=50,
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

    relevante = isRelevant(responseGPT, inpUser)

    if relevante:
        print(f"\n{responseGPT}")
        lastPrompts.append(inpUser)
        lastResponses.append(responseGPT)
    else:
        print("La respuesta no es relevante")
        print(f"\n{responseGPT}\n")