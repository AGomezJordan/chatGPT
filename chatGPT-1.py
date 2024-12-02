import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(
    api_key = APIKEY
)

model = "gpt-3.5-turbo"
prompt = "Elije un nombre para un elefante"
messages = [
    # {"role": "system", "content": "Eres un asistente creativo."},
    {"role": "user", "content": prompt}
]

response = client.chat.completions.create(
    model=model,
    messages=messages,
    n=3,
    temperature=0.5,
    max_tokens=20
)

print(response)
print()

# textGenerated = response.choices[0].message.content
# print(textGenerated)

for idx, choice in enumerate(response.choices):
    textGenerated = choice.message.content
    print(f"Respose {idx + 1}: {textGenerated}\n")