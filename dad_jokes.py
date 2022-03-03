import requests
import json
import sqlite3

connect = sqlite3.connect('dad-jokes.sqlite')
curson = connect.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS jokes 
               (id INTEGER PRIMARY KEY AUTOINCREMENT, 
               type VARCHAR(40),
               setup VARCHAR(40),
               punchline VARCHAR(40)
               )''')

userInput = int(input("Enter the number by joke type: 1 = Programming, 2 = Knock-knock, +3 = General : "))

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

response = requests.get(url, headers=headers)
responseJson = response.json()
with open('jokes.json', 'w') as f:
    json.dump(responseJson, f, indent=4)
    
jokesList = []
for i in responseJson['body']:
    type = i['type']
    setup = i['setup']
    punchline = i['punchline']
    data = (type,setup,punchline)
    jokesList.append(data)

connection.executemany('''INSERT INTO jokes (type,setup,punchline) VALUES(?,?,?)''', jokesList)
connection.commit()
connection.close()


