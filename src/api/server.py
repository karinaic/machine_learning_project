from flask import Flask, request, render_template, jsonify
import argparse
import requests
import os
import sys
from flask import send_from_directory

path = os.path.abspath(__file__) 
dir = os.path.dirname

src_path = dir(dir(path)) + os.sep + "utils"
sys.path.append(src_path)
import apis_tb

# Mandatory
app = Flask(__name__)  # __name__ --> __main__  

# ---------- Flask functions ----------

@app.route("/")  
def home():
    json_file = apis_tb.read_json(fullpath=settings_json)
    return json_file

path = os.path.abspath(__file__) 
dir = os.path.dirname
settings_json = dir(dir(dir(path))) + os.sep + 'reports' + os.sep + "data_cleaned.json"

@app.route("/recibe_informacion")
def recibe_info():
    pass 

#---------- Other functions ----------

def main():
    
    print("---------STARTING PROCESS---------")

    settings_file = dir(path) + os.sep + "settings.json"
        #print(settings_file)
        # Load json from file
    json_readed = apis_tb.read_json(fullpath=settings_file)

    # Load variables from jsons
    SERVER_RUNNING = json_readed["server_running"]

    DEBUG = json_readed["debug"]
    HOST = json_readed["host"]
    PORT_NUM = json_readed["port"]
    app.run(debug=DEBUG, host=HOST, port=PORT_NUM)

if __name__ == "__main__":
    main()