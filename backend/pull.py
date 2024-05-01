from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Mike:Mikedev88@studygroup.zvgkeux.mongodb.net/?retryWrites=true&w=majority&appName=Studygroup"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Select the database
db = client['Studygroup']

# Select the collection
collection = db['Users']

collection2 =db['Notes']

def pull_user():
    largest_id_document = collection.find_one(sort=[("_id", -1)]) 
    if largest_id_document:
        print("The largest _id is:", largest_id_document['_id'])
    else:
        print("No documents found in the collection.")
    return largest_id_document

def pull_doc():
    largest_id_document = collection2.find_one(sort=[("_id", -1)]) 
    if largest_id_document:
        print("The largest Notes _id is:", largest_id_document['_id'])
    else:
        print("No documents found in the collection.")
    return largest_id_document

pull_user()
pull_doc()