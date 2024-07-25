#render_template for html template
#url_for generate url 
#request access todo / documents
#redirect use to redirct student index page
from flask import Flask, render_template, url_for, request, redirect, session, flash, jsonify
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import google.generativeai as genai
from bson.objectid import ObjectId
import time
import threading
import os

genai.configure(api_key="AIzaSyCUXEfHA5OvN6Y41kEVaOVHPf5ayq8-2oo")
model = genai.GenerativeModel('gemini-pro')

uri = "mongodb+srv://Mike:Mikedev88@studygroup.zvgkeux.mongodb.net/?retryWrites=true&w=majority&appName=Studygroup"
app = Flask(__name__, static_folder='static')
app.secret_key = "your_secret_key_here"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client['Studygroup']
notes = db['Notes']
usersc = db['Users']
classes = db['Classes']

"""
def txt(class_id=None):
    query = {}
    if class_id:
        query['class'] = class_id  # Filtering by class if class_id is provided
    text = []
    for note in notes.find(query, {'content': 1, '_id': 0}):  # Exclude _id from the results
        if 'content' in note:
            text.append(" " + note['content'] + " ")
    return text
"""
def txt():
    text = []
    #find first is the search criteria {} rules what docs are teken, second is the value your taking Projection what your going to return
    for note in notes.find({'class': session['classid']}, {'content': 1, '_id': 0}): #need to put in the first scope look lik this {'class':'43'}
        if 'content' in note: 
            text.append(" "+note['content']+" ")
    return text

#def generate_unique_class_id():
    #while True:
        #for i in classes.find({},{"_id":1, "students":0, "class":0}):
            #class_id = ObjectId(os.urandom(12).hex())
            #newclassid = {"$set" : {'_id': class_id}}
            #if not classes.find_one({'_id': class_id}):
                #classes.update_one(i,newclassid)
        #time.sleep(10)

#t1=threading.Thread(target=generate_unique_class_id)          

def generate_best_note(notes):
    prompt = "Summarize and enhance the following notes: " + " ".join(notes)
    response = model.generate_content(prompt)
    return response.text


def send_note(doc): 
    response = model.generate_content("Create a summary out of this document and provide an example:" + doc)
    print(response.text)
    return response.text

def pull_user():
    largest_id_document = usersc.find_one(sort=[("_id", -1)]) 
    if largest_id_document:
        print("The largest _id is:", largest_id_document['_id'])
    else:
        print("No documents found in the collection.")
    return largest_id_document

def pull_doc():
    largest_id_document = notes.find_one(sort=[("_id", -1)]) 
    if largest_id_document:
        print("The largest Notes _id is:", largest_id_document['_id'])
    else:
        print("No documents found in the collection.")
    return largest_id_document

def pull_class():
    largest_id_document = classes.find_one(sort=[("_id", -1)]) 
    if largest_id_document:
        print("The largest Notes _id is:", largest_id_document['_id'])
    else:
        print("No documents found in the collection.")
    return largest_id_document

#home data to show data and submit todo items


@app.route("/")
@app.route("/login",methods=['GET','POST'])
def login():
    session.pop('username',None)
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        user = usersc.find_one({'Name': username, 'Pswd': password})
        if user:
            session['username'] = username
            msg = 'logged in successfully!'
            user_classes = list(classes.find({'students': session['username']}))
            return render_template('class_fold.html', msg=msg, classes=user_classes)
        else:
            msg='Incorrect Password/Username'
    return render_template('login.html',msg=msg)

@app.route("/register",methods=['GET','POST'])
def register():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        user = usersc.find_one({'Name': username})
        if user:
            msg = 'Account already exists !'
        elif not username or not password:
            msg = 'Please fill out the form !'
        else:
            usersc.insert_one({'Name': username, 'Pswd': password})
            msg = 'You have successfully registered!'
            return render_template('login.html',msg=msg)
    return render_template('register.html',msg=msg)



#---------------Michael SHEEESH -------------------------------
@app.route('/class_fold')
def class_fold():
    # Assuming you fetch classes or other data needed for the class fold page
    session.pop('classid',None)
    user_classes = list(classes.find({'students': session['username']}))
    return render_template('class_fold.html', classes=user_classes)

@app.route("/class_fold",methods=['GET','POST'])
def create_class():
    if request.method == 'POST':
        classtype = request.form['class_name']
        class_id = classes.insert_one({'students': [session['username']], 'class': classtype}).inserted_id
        usersc.update_one({'Name': session['username']},{'$addToSet': {'classes': class_id}})
    #all_notes = notes.find()
    user_classes = list(db.Classes.find({'students': session['username']}))
    return render_template('class_fold.html', classes=user_classes)

@app.route("/add_class",methods=['GET','POST'])
def add_class():
    if request.method == 'POST':
        class_id = request.form['classid']
        if classes.find_one({'_id': ObjectId(class_id)}) and not (usersc.find_one({'classes': ObjectId(class_id)})):
            classes.update_one({'_id': ObjectId(class_id)}, {'$addToSet': {'students': session['username']}})
            usersc.update_one({'Name': session['username']}, {'$addToSet': {'classes': ObjectId(class_id)}})
    return redirect(url_for('class_fold'))

@app.route('/showclasses')
def show_classes():
    user_classes = list(classes.find({'students': session['username']}))
    return render_template('class_fold.html', classes=user_classes)


@app.route('/class_details/<id>')
def class_details(id):
    class_info = classes.find_one({'_id': ObjectId(id)})
    if class_info:
        return render_template('class_details.html', class_info=class_info)
    else:
        flash('Class not found', 'error')
        return redirect(url_for('show_classes'))



@app.route("/createnote",methods=['GET','POST'])
def createnote():
    if request.method == 'POST':
        content = request.form['content']
        result=notes.insert_one({'created_by':(session['username']), 'title': content,'content': "",'shared_with':"",'class': session['classid']})
        note_id=result.inserted_id
        return redirect(url_for('edit_note', id=note_id))
    class_id = request.args.get('id')
    if (class_id!=None):
        session['classid']=request.args.get('id')
    all_notes = notes.find({'class': session['classid']})
    user_classes = [classes.find_one({'_id': ObjectId(class_id)})]
    summary = session.pop('summary', None)
    return render_template('createnote.html', Notes=all_notes, summary=summary, classes=user_classes)

@app.route("/<id>/sent/")
def sent(id):
    doc = notes.find_one({'_id': ObjectId(id)})
    if not doc:
        flash('Note not found', 'error')
        return redirect(url_for('createnote'))
    summary = send_note(doc['content'])
    flash(f'Summary: {summary}', 'info')
    session['summary'] = summary 
    return redirect(url_for('createnote'))


@app.route("/edit_note/<id>", methods=['GET', 'POST'])
def edit_note(id):
    note = notes.find_one({'_id': ObjectId(id)})
    if not note:
        flash('Note not found', 'error')
        return redirect(url_for('createnote'))

    # Check if the current user is the creator or is in the shared_with list
    current_user = session.get('username')
    if note['created_by'] != current_user and current_user not in note['shared_with']:
        flash('Access denied', 'error')
        return redirect(url_for('createnote'))

    if request.method == 'POST':
        new_content = request.form.get('content', '')
        notes.update_one({'_id': ObjectId(id)}, {'$set': {'content': new_content}})
        flash('Note updated successfully', 'success')
        return redirect(url_for('createnote'))

    return render_template('edit_note.html', note=note)


@app.route('/shownotes', methods=['GET'])
def show_notes():
    all_notes_byuser = list(notes.find({'created_by': session['username']}))
    all_sharedtouser = list(notes.find({'shared_with': session['username']}))
    all_notes_byuser+=all_sharedtouser
    summary = session.pop('summary', None)
    return render_template('createnote.html', Notes=all_notes_byuser, summary=summary)


@app.route("/note/<id>")
def show_note(id):
    note = notes.find_one({'_id': ObjectId(id)})
    if not note:
        flash('Note not found', 'error')
        return redirect(url_for('createnote'))
    return render_template('show_note.html', note=note)


@app.route('/summarize_selected', methods=['POST'])
def summarize_selected():
    data = request.get_json()
    selected_text = data.get('text', '')

    if not selected_text:
        return jsonify({'error': 'No text selected'}), 400

    # Use send_note function to generate the summary
    summary = send_note(selected_text)
    return jsonify({'summary': summary})

def summarize_function(content):
    # Implement your summarization logic here
    return content[:100]  # Example: returning the first 100 characters

@app.route("/bestnote/<class_id>")
def create_bestnote(class_id):
    # Here, fetch all notes for a given class ID or similar criteria
    notes_data = txt()  # Assuming txt() fetches the relevant notes implent the class_id
    if not notes_data:
        flash('No notes found for this class.', 'info')
        return redirect(url_for('createnote'))
    
    # Generate the best note
    best_note = generate_best_note(notes_data)
    return render_template('best_note.html', best_note=best_note, Notes=notes_data)



#t1.start()
if __name__ == '__main__':
    app.run(debug=True)
    
