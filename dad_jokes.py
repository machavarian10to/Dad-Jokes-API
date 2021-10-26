
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

t = int(input("შეიყვანე რიცხვი ხუმრობის ტიპის მიხედვით - (1=Programming, 2=Knock-knock, +3=General): "))
if t == 1:
    ty = 'programming'
elif t == 2:
    ty = 'knock-knock'
else:
    ty = 'general'

url = f"https://dad-jokes.p.rapidapi.com/joke/type/{ty}"

headers = {
    'x-rapidapi-key': "bee210a987mshb678b89635fc908p125930jsn1f1e186bbe0b",
    'x-rapidapi-host': "dad-jokes.p.rapidapi.com"
    }

resp = requests.get(url, headers=headers)

# დავალება 1
# print(resp)
# print(resp.text)
# print(resp.headers)
# print(resp.status_code)

# დავალება 2,3
# res = resp.json()
# with open('jokes.json', 'w') as f:
#     json.dump(res,f, indent=4)
#
# print(res['body'][0]['setup'])
# print(res['body'][0]['punchline'])

# დავალება 4
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


