from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
import creation_calls
import gemini
import pull


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"]= "Content-Type"



app.route('/Pull',methods =["POST","GET"])
def Pull():
    if request.method == "GET":
        content = request.args.get("Name")
    else:
        content = request.json.get("Name")
    x = pull.pull_user(content)
    #here I need to do the pymongo here 
    return jsonify(x)

"""def Pull():
    content = request.args.get("name")
    mydb = sqlite3.connect("thisdirectory/mydatabasedb")  # corrected line
    mycursor = mydb.cursor()
    myDetails = mycursor.execute(SELECT*From Info where Name ='{name}'.format(name = content))
    return jsonify
"""

app.route('/Pull',methods =["Post","GET"])
def Push():   
    content = request.get_json()
    creation_calls.create_user(content)
    return "push initiated"

if __name__ == "__main__":
    app.run()