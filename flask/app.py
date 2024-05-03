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
notes = db['Notes']
collection2 = db['Users']

#home data to show data and submit todo items
@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        notes.insert_one({'userid':"Michael", 'content': content})
    #this will render the frontend
    all_notes = notes.find()
    return render_template('index.html', Notes = all_notes)


if __name__ == '__main__':
    app.run(debug=True)