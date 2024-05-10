
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import google.generativeai as genai
from bson import ObjectId

genai.configure(api_key="AIzaSyCUXEfHA5OvN6Y41kEVaOVHPf5ayq8-2oo")
model = genai.GenerativeModel('gemini-pro')

uri = "mongodb+srv://Mike:Mikedev88@studygroup.zvgkeux.mongodb.net/?retryWrites=true&w=majority&appName=Studygroup"


client = MongoClient(uri, server_api=ServerApi('1'))
db = client['Studygroup']
notes = db['Notes']
usersc = db['Users']

def txt():
    text = []
    #find first is the search criteria {} rules what docs are teken, second is the value your taking Projection what your going to return
    for note in notes.find({}, {'content': 1}): #need to put in the first scope look lik this {'class':'43'}
        if 'content' in note: 
            text.append(" "+note['content']+" ") 
    return text
text = txt()


print(text)

def generate_best_note(notes):
    # Create a comprehensive prompt from all notes
    prompt = "Summarize and enhance the following notes: " + " ".join(notes)
    # Generate content using the AI model
    response = model.generate_content(prompt)
    return response.text


best_note = generate_best_note(text)

print(best_note)


