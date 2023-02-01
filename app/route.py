from flask import render_template, request, redirect, url_for, jsonify
from .db import get_db_config, db_connect
import mysql.connector
from app import app
 



# Parametre de connection a la BDD
path = "./config.json"
config = get_db_config(path)

# Connection a la BDD
myDB = db_connect(config)
cursor = myDB.cursor()
dbOK = myDB.is_connected()


# On a differents chemins pour afficher nos données de la BDD ou pour utiliser une des methodes CRUD 
# Le /materiel a la suite de l'url nous permets d'afficher 1 ou l'ensemble des materiels
# Si on ajoute un id a la suite (ex : /materiel/1) on peut voir un élément en particulier
# Meme méthode pour employé avec le chemin /employe
# On Jsonify les valeurs que l'on veux insérer pour visionner/inserer correctement les données

@app.route('/', methods=["GET", "POST"])
def index():

    if request.method == "GET":

        try:
            query_1=""" SELECT * FROM `materiel`;"""
            cursor.execute(query_1)
            result_select_1 = cursor.fetchall()
            
            query_2="""SELECT * FROM `employe`;"""
            cursor.execute(query_2)
            result_select_2 = cursor.fetchall()            

            return render_template('index.html', configHTML=config, dbOK__=dbOK,
                HTML_Result=result_select_1, HTML_Result_2=result_select_2)
        

        except mysql.connector.Error as e:
            return render_template('index.html', configHTML=config, error=e)

# CRUD pour le materiel

# Get l'ensemble du materiel
@app.route('/materiel', methods=['GET'])
def get_materiel():
    query = """SELECT * FROM materiel"""
    cursor.execute(query)
    materiels = cursor.fetchall()
    tout_les_materiels = []
    for materiel in materiels:
        tout_les_materiels.append({"id":materiel[0], "nom":materiel[1], "taille":materiel[2], "etat":materiel[3]})
    return jsonify(tout_les_materiels)

# Get un materiel
@app.route('/materiel/<int:id>', methods=['GET'])
def get_materiel_id(id):
    query = """SELECT * FROM materiel WHERE id = {}""".format(id)
    cursor.execute(query)
    materiel = cursor.fetchone()
    return jsonify({"id":materiel[0], "nom":materiel[1], "taille":materiel[2], "etat":materiel[3]})

# Post un materiel
@app.route('/materiel', methods=['POST'])
def post_materiel():
    data = request.get_json()
    query = f"""INSERT INTO materiel (nom,taille,etat) VALUES ("{data["nom"]}", "{data["taille"]}", "{data["etat"]}")"""
    cursor.execute(query)
    myDB.commit()
    return jsonify("materiel ajouté avec succès"), 201

# Put un materiel
@app.route('/materiel/<int:id>', methods=['PUT'])
def put_materiel(id):
    data = request.get_json()
    query = f"""UPDATE materiel SET nom = '{data["nom"]}', taille = '{data["taille"]}', etat = '{data["etat"]}' WHERE id = {id}"""
    cursor.execute(query)
    myDB.commit()
    return jsonify("materiel modfié avec succès")

# Delete un materiel
@app.route('/materiel/<int:id>', methods=['DELETE'])
def delete_materiel(id):
    query = """DELETE FROM materiel WHERE id = {}""".format(id)
    cursor.execute(query)
    myDB.commit()
    return jsonify("materiel supprimé avec succès")



# CRUD pour les employe

#Get les employes
@app.route('/employe', methods=['GET'])
def get_employe():
    query = """SELECT * FROM employe"""
    cursor.execute(query)
    employe = cursor.fetchall()
    tout_les_employes = []
    for materiel in employe:
        tout_les_employes.append({"id":materiel[0], "nom":materiel[1], "prenom":materiel[2], "age":materiel[3], "departement":materiel[4]})
    return jsonify(tout_les_employes)

# Get Un employe
@app.route('/employe/<int:id>', methods=['GET'])
def get_employe_id(id):
    query = """SELECT * FROM employe WHERE id = {}""".format(id)
    cursor.execute(query)
    item = cursor.fetchone()
    return jsonify({"id":item[0], "nom":item[1], "prenom":item[2],
        "age":item[3], "departement":item[4]})

# Post les employes
@app.route('/employe', methods=['POST'])
def post_employe():
    data = request.get_json()
    query = """INSERT INTO employe (nom, prenom, age, departement) VALUES ('{}', '{}',
        '{}', '{}')""".format(data["nom"], data["prenom"], data["age"], data["departement"])
    cursor.execute(query)
    myDB.commit()
    return jsonify("Employé ajouté avec succés"), 201

# Put UN employe
@app.route('/employe/<int:id>', methods=['PUT'])
def put_employe(id):
    data = request.get_json()
    query = """UPDATE employe SET nom = '{}', prenom = '{}', age = '{}',
        departement = '{}' WHERE id = {}""".format(data["nom"], data["prenom"], data["age"], data["departement"], id)
    cursor.execute(query)
    myDB.commit()
    return jsonify("Employé modifier avec succès")

# Delete UN employe
@app.route('/employe/<int:id>', methods=['DELETE'])
def delete_employe(id):
    query = """DELETE FROM employe WHERE id = {}""".format(id)
    cursor.execute(query)
    myDB.commit()
    return jsonify("Employé supprimé avec succès")