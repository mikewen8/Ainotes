#render_template for html template
#url_for generate url 
#request access todo / documents
#redirect use to redirct student index page
from flask import Flask, render_template, url_for, request, redirect, session
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import google.generativeai as genai
genai.configure(api_key="AIzaSyCUXEfHA5OvN6Y41kEVaOVHPf5ayq8-2oo")
model = genai.GenerativeModel('gemini-pro')

uri = "mongodb+srv://Mike:Mikedev88@studygroup.zvgkeux.mongodb.net/?retryWrites=true&w=majority&appName=Studygroup"
app = Flask(__name__)
app.secret_key = "your_secret_key_here"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client['Studygroup']
notes = db['Notes']
usersc = db['Users']
def pull_user():
    largest_id_document = notes.find_one(sort=[("_id", -1)]) 
    if largest_id_document:
        print("The largest _id is:", largest_id_document['_id'])
    else:
        print("No documents found in the collection.")
    return largest_id_document

def pull_doc():
    largest_id_document = usersc.find_one(sort=[("_id", -1)]) 
    if largest_id_document:
        print("The largest Notes _id is:", largest_id_document['_id'])
    else:
        print("No documents found in the collection.")
    return largest_id_document

#home data to show data and submit todo items


@app.route("/")
@app.route("/login",methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        user = usersc.find_one({'Name': username, 'Pswd': password})
        if user:
            session['username'] = username
            msg = 'logged in successfully!'
            return render_template('createnote.html', msg=msg)
        else:
            msg='Incorrect Password/Username'
    return render_template('login.html',msg=msg)

@app.route("/createnote",methods=['GET','POST'])
def createnote():
    if request.method == 'POST':
        content = request.form['content']
        id=notes.find_one(sort=[("_id", -1)]) 
        id['_id']+=1
        notes.insert_one({'_id':id['_id'],'username':(session['username']), 'content': content})
    #this will render the frontend
    all_notes = notes.find()
    return render_template('createnote.html', Notes = all_notes)


if __name__ == '__main__':
    app.run(debug=True)
    