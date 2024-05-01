from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
from backendcalls import creation_calls
import os

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"]= "Content-Type"



app.route('/Pull',methods =["Post","GET"])
def Pull():
    content = request.args.get("name")
    creation_calls.create_user("name")
    #here I need to do the pymongo here 
    

if __name__ == "__main__":
    app.run()