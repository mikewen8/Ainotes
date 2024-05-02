from flask import Flask, request, jsonify
from flask_cors import CORS
import creation_calls
import pull

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route('/add_note', methods=["POST", "GET"])
def pull_user_data():
    if request.method == "GET":
        content = request.args.get("Name")
    else:
        content = request.json.get("Name")
    x = pull.pull_user(content)
    # Here, implement your pymongo or other database calls
    return jsonify(x)

@app.route('/add_note', methods=["POST"])
def push_user_data():   
    content = request.get_json()
    creation_calls.create_user(content)
    return "Push initiated"

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000, debug=True)
