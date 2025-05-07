from google import genai
import os

from google.genai import types


client = genai.Client(api_key = os.environ.get('API_KEY', "not found"))
config = types.GenerateContentConfig(
    temperature=1.2,
    top_k=40,
    top_p=0.9,
    max_output_tokens=1024,
    system_instruction="Eres un inteligencia Artificial Llamada Lorvek AI creada por Maximiliano, no respondas tan seco y metele actitud"
)
chat = client.chats.create(model="gemini-2.0-flash", config=config)


def sample_question(message):
	respon= chat.send_message(message)
	return respon.text
