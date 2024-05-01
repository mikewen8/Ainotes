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
    if request.method == "GET":
        content = request.args.get("Name")
    else:
        content = request.json.get("Name")
    x = pull.pull_user(content)
    #here I need to do the pymongo here 
    return jsonify(x)


app.route('/Pull',methods =["Post","GET"])
def Push():   
    content = request.get_json()
    creation_calls.create_user(content)
    return "push initiated"

if __name__ == "__main__":
    app.run()