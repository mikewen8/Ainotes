#render_template for html template
#url_for generate url 
#request access todo / documents
#redirect use to redirct student index page
from flask import Flask, render_template, url_for, request, redirect
from pymongo import MongoClient
from pymongo.server_api import ServerApi

import google.generativeai as genai
genai.configure(api_key="AIzaSyCUXEfHA5OvN6Y41kEVaOVHPf5ayq8-2oo")
model = genai.GenerativeModel('gemini-pro')

uri = "mongodb+srv://Mike:Mikedev88@studygroup.zvgkeux.mongodb.net/?retryWrites=true&w=majority&appName=Studygroup"
app = Flask(__name__)

client = MongoClient(uri, server_api=ServerApi('1'))
db = client['Studygroup']
collection = db['Notes']
collection2 = db['Users']

def add_doc(doc):
    try:
        result = collection.insert_one(doc)
        print("Inserted document id:", result.inserted_id)
    except Exception as e:
        print("An error occurred:", e)

def add_user(user):
    try:
        result = collection2.insert_one(user)
        print("Inserted document id:", result.inserted_id)
    except Exception as e:
        print("An error occurred:", e)
        
def pull_user():
    largest_id_document = collection2.find_one(sort=[("_id", -1)]) 
    if largest_id_document:
        print("The largest _id is:", largest_id_document['_id'])
    else:
        print("No documents found in the collection.")
    return largest_id_document

def pull_doc():
    largest_id_document = collection.find_one(sort=[("_id", -1)]) 
    if largest_id_document:
        print("The largest Notes _id is:", largest_id_document['_id'])
    else:
        print("No documents found in the collection.")
    return largest_id_document

def send_note(doc): 
    response = model.generate_content("Create a summary out of this document:" + doc)
    print(response.text)
    return response.text

#home data to show data and submit todo items
@app.route("/",method=['GET','POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        u_id=pull_user
        collection.insert_one({'_id':1,'userid':u_id,'note':content})
    #this will render the frontend
    all_notes = collection.find()
    return render_template('index.html', collection = all_notes)


if __name__ == '__main__':
    app.run(debug=True)