
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
    for note in notes.find({'class':'132'}, {'content': 1}): 
        if 'content' in note: 
            text.append(" "+note['content']+" ") 
    return text

text = txt()
print(text)


