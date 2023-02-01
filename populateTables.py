from app.db import get_db_config, db_connect
import mysql.connector
from app import app
import json


# Parametre de connection a la BDD a l'aide du fichier config.json qui sera notre chemin
path = "./config.json"
config = get_db_config(path)

# Connection a la BDD
myDB = db_connect(config)
cursor = myDB.cursor()
dbOK = myDB.is_connected()


if __name__ == "__main__":
    pass

# Chargement de data.json encodé en utf-8 pour l'insertion dans notre BDD des éléments dans le fichier
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)




# Insertion des elements dans la BDD
for item in data['materiel']:
    for key, value in item.items():
        try:
            query = (f"""INSERT INTO materiel (nom, dimension, etat) VALUES ("{value[0]}", "{value[1]}", "{value[2]}")""")
            print(query)
            cursor.execute(query)
            myDB.commit()
        except mysql.connector.Error as e:
            print(e)

for item in data['employe informatique']:
    for key, value in item.items():
        try:
            query = (f"""INSERT INTO employe (nom, prenom, age, departement) VALUES ("{value[0]}", "{value[1]}", "{value[2]}", "{value[3]}")""")
            print(query)
            cursor.execute(query)
            myDB.commit()
        except mysql.connector.Error as e:
            print (e)