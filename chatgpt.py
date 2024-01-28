from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv()
client = OpenAI(api_key=os.environ.get("KEY",""))
prompt = """
Eres un narrador de historias
EL usuario solo va a conocer una parte de la historia y te va a hacer unas preguntas para descubrir el resto de la historia y tienes que reponder si o no
Mucho tiempo atrás, cuatro hombres se encontraron en un situación desesperada, a la deriva en mar abierto sobre el tronco de un arbol. Su barco se había hundido. Sin nada que comer acordaron que cada uno de ellos se sacrificaría un brazo. Fueron rescatados ates del turno del cuarto hombre. Los otros tres recordaron su promesa y piedieron uno de sus brazos. Como él vivía lejos de ellos, no tenia la menor intención de cumplir su promesa. Pueso un anuncio en la prensa ofreciendo un millón de euros a cualquiera que le diera uno de sus brazos. Pronto encontró un voluntario
Un hombre envuelve un brazo cortado y envia el paquete a tres hombres con un solo brazo. Satisfechos con el contenido del paquete , los hombres arrojan el brazo al mar
"""
messages = [
    {"role": "system", "content": "Hola"},
    {"role": "user", "content": "Cuenta la historia que tiene que conocer el usuario"}
  ]
while True:
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
    )
    print(response.choices[0].message.content)
    {'role':'system','content':response.choices[0].message.content}
    new_message = {"role": "user", "content": input("Escribe algo: ")}
    messages.append(new_message)