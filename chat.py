import clase



prompt = """
Eres un narrador de historias
EL usuario solo va a conocer una parte de la historia y te va a hacer unas preguntas para descubrir el resto de la historia y tienes que justificar primero yluego responder si o no
Esta es la historia que va a conocer el usuario <Un hombre envuelve un brazo cortado y envia el paquete a tres hombres con un solo brazo. Satisfechos con el contenido del paquete , los hombres arrojan el brazo al mar>
Esta es la historia completa que el usuario tiene que ir descubriendo <Mucho tiempo atrás, cuatro hombres se encontraron en un situación desesperada, a la deriva en mar abierto sobre el tronco de un arbol. Su barco se había hundido. Sin nada que comer acordaron que cada uno de ellos se sacrificaría un brazo. Fueron rescatados ates del turno del cuarto hombre. Los otros tres recordaron su promesa y pidieron uno de sus brazos. Como él vivía lejos de ellos, no tenia la menor intención de cumplir su promesa. Puso un anuncio en la prensa ofreciendo un millón de euros a cualquiera que le diera uno de sus brazos. Pronto encontró un voluntario>
Ej: Pregunta: ¿Los hombres se conocian? Respuesta {justificacion:'Los hombres estaban a la deriva en mar abierto por lo tanto se conocian' respuesta':Sí}
Ej: Pregunta: ¿El hombre que envia el paquete compra el brazo? Respuesta {justificacion:'El hombre que envia el brazo se lo compra a una pesona que ve el anuncio en el periodico por 1 millon de euros' respuesta':Sí}
Ej: Pregunta ¿El brazo es del hombre que envia el paquete? Respuesta {justificacion:'EL hombre compro el brazo por lo tanto no era suyo' respuesta':'No'}
"""
prompt2 = """
Esta es una lista de cosas que tiene que descubrir el usuario ara ganar cuando las descubra todas tienes que decirle que ha ganado:
  -Los cuatro hombres se encontraron a la deriva en el mar
  -Tres hombres se cortaron un brazo para comer y antes de que se lo fuese a cortar el cuarto les rescataron
  -Los tres hombres le piedieron su brazo al hombre
  -EL brazo no es del hombre
  -El hombre saco el brazo de una persona que vio su anuncio en el periodico
"""


messages = [
    {"role": "system", "content": "You are a helpful assistant designed to output JSON."}
]




Chat = clase.Chat(messages)
while True:
    print(Chat.send_message(input("Escribe algo: ")))