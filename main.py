import clase
import random
from record_voice import grabar

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

def hacer_hechos(hechos):
  hechosbien = ""
  for i in range(len(hechos)):
    hechosbien += "Hecho" + str(i+1) + ": " + str(hechos[i]) + "\n"
  return hechosbien   

def dopropmt(historia_larga, historia_corta, hechos: list, ejemplos):

  ejemplosbien = ""
  for ejemplo in ejemplos:
     ejemplosbien += ejemplo + "\n"

    
  prompt = """
  Eres un narrador de historias
  EL usuario solo va a conocer una parte de la historia y te va a hacer unas preguntas para descubrir el resto de la historia y tienes que justificar primero yluego responder si o no
  Esta es la historia que va a conocer el usuario <{}>
  Esta es la historia completa que el usuario tiene que ir descubriendo <{}>
  """.format(historia_corta,historia_larga)

  a = """{justificacion:"", respuesta:"siono", Hecho1:"Boolean", Hecho2:"Boolean", Hecho3:"Boolean", Hecho4:"Boolean", Hecho5:"Boolean", Hecho6:"Boolean"}"""

  prompt2 = """
  Esta es una lista de hechos que tiene que descubrir el usuario para ganar y tienes que poner True si lo ha descubierto y False si no lo ha descubierto:
  {}
  Plantilla de respuesta {}

  {}
  """.format(hechos,a,ejemplosbien)

  return prompt + "\n" + prompt2

def juego(historia):

  hechos = hacer_hechos(historia.milestones)

  messages = [
      "Eres un experto distinguiendo si un usuario a descubierto cosas de una historia. Vas a responder en JSON",dopropmt(historia.historia_larga,historia.historia_corta,hechos,historia.ejemplos)
  ]

  print("Esta es la historia \"{}\"".format(historia.historia_corta))

  Chat = clase.Chat(messages)
  while True:
      input("Pulsa ENTER para grabar")
      respuesta = Chat.send_message(grabar())
      if respuesta["respuesta"] in ["Sí","Si","si","sí"]:
        print(random.choice(formas_de_decir_si))
      else:
        print(random.choice(formas_de_decir_no))
      for i in range(1,7):
          if respuesta['Hecho'+str(i)] == 'True':
            hechos['Hecho'+str(i)] = respuesta['Hecho'+str(i)]
      if len(hechos) >= 5:
        print("Has ganado")
        break
