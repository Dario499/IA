import psycopg2
import typer
import random
from dotenv import load_dotenv
import os
import maincopy
import psycopg2.extras



load_dotenv()

app = typer.Typer()

conn = psycopg2.connect(dbname=os.environ.get("DB",""), user=os.environ.get("USER",""),password=os.environ.get("PASSWORD",""),host=os.environ.get("HOST",""))

cur = conn.cursor()

@app.command()
def new_story():
    large_story: str = input("Historia larga: ")
    short_story: str = input("Historia corta: ")
    name: str = input("Nombre de la historia: ")
    cur.execute("""INSERT INTO stories (large_story, short_story, name) VALUES ('{}','{}','{}')""".format(large_story,short_story,name))
    conn.commit()

@app.command()
def new_milestone():
    descripcion: str = input("Descripción: ")
    id_historia: str = input("ID de la historia: ")
    cur.execute("""INSERT INTO milestones (story_id,description) VALUES ('{}','{}')""".format(id_historia,descripcion))
    conn.commit()

@app.command()
def new_example():
    descripcion: str = input("Descripción: ")
    id_historia: str = input("ID de la historia: ")
    cur.execute("""INSERT INTO examples (story_id, example) VALUES ('{}','{}')""".format(id_historia, descripcion))
    conn.commit()

@app.command()
def play_story():
    cur.execute("SELECT * FROM stories")
    historia = random.choice(cur.fetchall())
    uuid = historia[0]
    cur.execute("SELECT * FROM examples WHERE story_id = %s",(str(uuid),))
    ejemplos = []
    for ejemplo in cur.fetchall():
        ejemplos.append(ejemplo[2])
    cur.execute("SELECT * FROM milestones WHERE story_id = %s",(str(uuid),))
    milesotnes = []
    for milestone in cur.fetchall():
        milesotnes.append(milestone[2])
    maincopy.juego(historia[1],historia[2],milesotnes,ejemplos)
    



app()