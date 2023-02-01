import mysql.connector

#Creation des 2 tables Materiel/Employé pour la BDD API_CHU 

# Connection à la BDD
myDB = mysql.connector.connect(user='root', password='example', host='localhost', port= 3307, database='API_CHU')
cursor = myDB.cursor()

# Creation de la table materiel
create_materiel_table = '''
CREATE TABLE materiel (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    dimension VARCHAR(255) NOT NULL,
    etat VARCHAR(255) NOT NULL
);
'''
cursor.execute(create_materiel_table)

# Creation de la table employe
create_employe_table = '''
CREATE TABLE employe (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255) NOT NULL,
    prenom VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    departement VARCHAR(255) NOT NULL
);
'''
cursor.execute(create_employe_table)

# fermer le cursor et la connection
cursor.close()
myDB.close()