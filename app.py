from app import app, route
from db import get_db_config

tester_config = False

if __name__ == "__main__":
    if(tester_config):
        config = get_db_config("config.json")
    
    app.run(debug = True, host="0.0.0.0")