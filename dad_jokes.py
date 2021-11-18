import requests
import json
import sqlite3

conn = sqlite3.connect('dad-jokes.sqlite')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS jokes 
               (id INTEGER PRIMARY KEY AUTOINCREMENT, 
               type VARCHAR(40),
               setup VARCHAR(40),
               punchline VARCHAR(40)
               )''')

userInput = int(input("შეიყვანე რიცხვი ხუმრობის ტიპის მიხედვით - 1=Programming, 2=Knock-knock, +3=General : "))
if userInput == 1:
    jokeType = 'programming'
elif userInput == 2:
    jokeType = 'knock-knock'
else:
    jokeType = 'general'

url = f"https://dad-jokes.p.rapidapi.com/joke/type/{jokeType}"

headers = {
    'x-rapidapi-key': "bee210a987mshb678b89635fc908p125930jsn1f1e186bbe0b",
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
    }

resp = requests.get(url, headers=headers)
res = resp.json()
with open('jokes.json', 'w') as f:
    json.dump(res,f, indent=4)
lst = []
for i in res['body']:
    type = i['type']
    setup = i['setup']
    punchline = i['punchline']
    data = (type,setup,punchline)
    lst.append(data)

conn.executemany('''INSERT INTO jokes (type,setup,punchline) VALUES(?,?,?)''', lst)
conn.commit()
conn.close()


