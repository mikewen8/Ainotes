#need to bring in my call functions
from backendcalls import creation_calls,size
from flask import Flask, request, jsonify
import json

# Importing your custom modules
import backendcalls
import backendcalls.creation_calls
import backendcalls.pull


app = Flask(__name__)

@app.route('/add_user', methods=['POST'])
def receive_user():
    data = request.json
    new_id = backendcalls.pull.pull_user()["_id"] + 1
    data["_id"] = new_id
    backendcalls.creation_calls.add_user(data)
    return jsonify({"message": "User added", "user_id": new_id}), 201

@app.route('/add_doc', methods=['POST'])
def receive_doc():
    data = request.json
    new_doc_id = backendcalls.pull.pull_doc()["_id"] + 1
    data["_id"] = new_doc_id
    data["userid"] = backendcalls.pull.pull_user()["_id"] 
    backendcalls.creation_calls.add_doc(data)
    #201 status code
    return jsonify({"message": "Document added", "document_id": new_doc_id}), 201

if __name__ == '__main__':
    app.run(debug=True)
