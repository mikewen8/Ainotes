from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Mike:Mikedev88@studygroup.zvgkeux.mongodb.net/?retryWrites=true&w=majority&appName=Studygroup"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Select the database
db = client['Studygroup']

# Select the collection
collection = db['Users']

# Document to insert
#_id is user id but need to make it a primary key
"""
document = {
    "_id": 1,
    "Name": "Mike"
}
"""
# Insert the document into the collection
def add_user(user):
    try:
        result = collection.insert_one(user)
        print("Inserted document id:", result.inserted_id)
    except Exception as e:
        print("An error occurred:", e)
