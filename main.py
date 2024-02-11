import clase
import random

formas_de_decir_si = [
    "Sí",
    "Por supuesto",
    "Claro que sí",
    "Desde luego",
    "¡Por supuesto que sí!",
    "Indudablemente",
    "Absolutamente",
    "Así es",
    "Sin duda",
]

formas_de_decir_no = [
    "No",
    "De ninguna manera",
    "Para nada",
    "Jamás",
    "Nunca",
    "Lo siento, pero no",
    "Absolutamente no",
    "Negativo",
    "No lo creo",
    "Definitivamente no"
]

prompt = """
Eres un narrador de historias
EL usuario solo va a conocer una parte de la historia y te va a hacer unas preguntas para descubrir el resto de la historia y tienes que justificar primero yluego responder si o no
Esta es la historia que va a conocer el usuario <Un hombre envuelve un brazo cortado y envia el paquete a tres hombres con un solo brazo. Satisfechos con el contenido del paquete , los hombres arrojan el brazo al mar>
Esta es la historia completa que el usuario tiene que ir descubriendo <Mucho tiempo atrás, cuatro hombres se encontraron en un situación desesperada, a la deriva en mar abierto sobre el tronco de un arbol. Su barco se había hundido. Sin nada que comer acordaron que cada uno de ellos se sacrificaría un brazo. Fueron rescatados ates del turno del cuarto hombre. Los otros tres recordaron su promesa y pidieron uno de sus brazos. Como él vivía lejos de ellos, no tenia la menor intención de cumplir su promesa. Puso un anuncio en la prensa ofreciendo un millón de euros a cualquiera que le diera uno de sus brazos. Pronto encontró un voluntario>


"""
prompt2 = """
Esta es una lista de hechos que tiene que descubrir el usuario para ganar y tienes que poner True si lo ha descubierto y False si no lo ha descubierto:
Hecho1: Los cuatro hombres se encontraron a la deriva en el mar
Hecho2: Los cuatro acordaron cortarse un brazo para comer
Hecho3: Los tres hombres le piedieron su brazo al cuarto hombre
Hecho4: Rescataron a los hombres antes de que el cuarto se cortase el brazo
Hecho5: El hombre compro el brazo
Hecho6: Compro el brazo en el periodico

Plantilla de respuesta {justificación:"", respuesta:"siono", Hecho1:"Boolean", Hecho2:"Boolean", Hecho3:"Boolean", Hecho4:"Boolean", Hecho5:"Boolean", Hecho6:"Boolean"}

Ej: Pregunta: ¿Los hombres se conocian?
Respuesta 
  {justificacion:'Los hombres estaban a la deriva en mar abierto por lo tanto se conocian' respuesta':Sí, Hecho1:"False", Hecho2:"False", Hecho3:"False ", Hecho4:"False", Hecho5:"False", Hecho6:"False"}
Ej: Pregunta: ¿El hombre que envia el paquete compra el brazo?
Respuesta 
  {justificacion:'El hombre que envia el brazo se lo compra a una pesona que ve el anuncio en el periodico por 1 millon de euros' respuesta':Sí, Hecho1:"False", Hecho2:"False", Hecho3:"False ", Hecho4:"False", Hecho5:"True", Hecho6:"False"}
Ej: Pregunta: ¿El brazo es del hombre que envia el paquete? 
Respuesta
  {justificacion:'EL hombre compro el brazo por lo tanto no era suyo' respuesta':'No', Hecho1:"False", Hecho2:"False", Hecho3:"False ", Hecho4:"False", Hecho5:"False", Hecho5:"False"}
"""


messages = [
    "Eres un experto distinguiendo si un usuario a descubierto cosas de una historia. Vas a responder en JSON",prompt,prompt2
]

hechos = {}

print("Esta es la historia \"Un hombre envuelve un brazo cortado y envia el paquete a tres hombres con un solo brazo. Satisfechos con el contenido del paquete , los hombres arrojan el brazo al mar\"")

Chat = clase.Chat(messages)
while True:
    respuesta = Chat.send_message(input("Escribe algo: "))
    print(respuesta["respuesta"])
    for i in range(1,7):
        if respuesta['Hecho'+str(i)] == 'True':
          hechos['Hecho'+str(i)] = respuesta['Hecho'+str(i)]
    if len(hechos) >= 5:
       print("Has ganado")
       break