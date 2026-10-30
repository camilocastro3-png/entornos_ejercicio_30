from fastapi import FastAPI
from google import genai

app = FastAPI()

client = genai.Client()

@app.get("/chat/{saludo}")
def llamar_ia(saludo):
    instrucion = "hablame en ingles siempre" 
    inferencia = client.interactions.create(
        model="gemini-3.1-flash-lite",
        input= instrucion + saludo 
    )
    return {"Respuesta": inferencia.output_text }