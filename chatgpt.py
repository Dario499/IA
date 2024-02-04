import json
from dotenv import load_dotenv
import os
from openai import OpenAI

#Esta es la historia que va a conocer el usuario <Un hombre envuelve un brazo cortado y envia el paquete a tres hombres con un solo brazo. Satisfechos con el contenido del paquete , los hombres arrojan el brazo al mar>
load_dotenv()
client = OpenAI(api_key=os.environ.get("KEY",""))
prompt = """
Eres un narrador de historias
EL usuario solo va a conocer una parte de la historia y te va a hacer unas preguntas para descubrir el resto de la historia y tienes que justificar primero yluego responder si o no
Esta es la historia que va a conocer el usuario <Un hombre envuelve un brazo cortado y envia el paquete a tres hombres con un solo brazo. Satisfechos con el contenido del paquete , los hombres arrojan el brazo al mar>
Esta es la historia completa que el usuario tiene que ir descubriendo <Mucho tiempo atrás, cuatro hombres se encontraron en un situación desesperada, a la deriva en mar abierto sobre el tronco de un arbol. Su barco se había hundido. Sin nada que comer acordaron que cada uno de ellos se sacrificaría un brazo. Fueron rescatados ates del turno del cuarto hombre. Los otros tres recordaron su promesa y piedieron uno de sus brazos. Como él vivía lejos de ellos, no tenia la menor intención de cumplir su promesa. Pueso un anuncio en la prensa ofreciendo un millón de euros a cualquiera que le diera uno de sus brazos. Pronto encontró un voluntario>
Ej: Pregunta: ¿Los hombres se conocian? Respuesta {justificacion:'Los hombres estaban a la deriva en mar abierto por lo tanto se conocian' respuesta':Sí}
Ej: Pregunta: ¿El hombre que envia el paquete compra el brazo? Respuesta {justificacion:'El hombre que envia el brazo se lo compra a una pesona que ve el anuncio en el periodico por 1 millon de euros' respuesta':Sí}
"""
messages = [
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."},
    {"role": "system", "content": prompt},
    {"role": "user", "content": "¿El brazo cortado es del hombre que envia el paquete?"}
  ]
while True:
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },

    messages=messages
    )
    print(json.loads(response.choices[0].message.content))
    {'role':'system','content':response.choices[0].message.content}
    new_message = {"role": "user", "content": input("Escribe algo: ")}
    messages.append(new_message)