from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Mike:Mikedev88@studygroup.zvgkeux.mongodb.net/?retryWrites=true&w=majority&appName=Studygroup"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Select the database
db = client['Studygroup']

# Select the collection
collection = db['Notes']

# Document to insert
"""
document = {
    "_id": 3,
    "Name": "Mike",
    "Note": "This is the very third note and it is a very very long note, it can be a very long long note maybe a full essay woth of notes I'm trying to see how much storage this will take for this super super long note",
}
"""
# Insert the document into the collection
def add_doc(doc):
    try:
        result = collection.insert_one(doc)
        print("Inserted document id:", result.inserted_id)
    except Exception as e:
        print("An error occurred:", e)

