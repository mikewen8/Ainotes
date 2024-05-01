from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
from backendcalls import creation_calls,pull
import os

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"]= "Content-Type"



app.route('/Pull',methods =["Post","GET"])
def Pull():
    content = request.args.get("Name")
    pull.pull_user(content)
    #here I need to do the pymongo here 
    return jsonify({"message": "Data pulled successfully"})


app.route('/Pull',methods =["Post","GET"])
def Push():   
    content = request.get_json()
    creation_calls.create_user(content)

if __name__ == "__main__":
    app.run()