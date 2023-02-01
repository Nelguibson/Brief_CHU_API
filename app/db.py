import json
import mysql.connector

def get_db_config(chemin):
    f = open(chemin, "r")
    config = json.load(f)
    f.close
    return config

def db_connect(config):
    try:
        db = mysql.connector.connect(**config)

        return db

    except Exception as e:
        print(e)