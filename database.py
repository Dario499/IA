import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(dbname=os.environ.get("DB",""), user=os.environ.get("USER",""),password=os.environ.get("PASSWORD",""),host=os.environ.get("HOST",""))

cur = conn.cursor()

cur.execute("INSERT INTO stories VALUES (large_story)", ("as","fdfsa","dfasd"))



cur.execute("SELECT * FROM stories;")
print(cur.fetchone())