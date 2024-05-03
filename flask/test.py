from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection URI
uri = "mongodb+srv://Mike:Mikedev88@studygroup.zvgkeux.mongodb.net/?retryWrites=true&w=majority&appName=Studygroup"

def insert_initial_document(uri):
    try:
        # Connect to MongoDB
        client = MongoClient(uri)
        db = client['Studygroup']
        collection = db['Notes']
        
        # Insert a document
        initial_document = {
            'userid': 'initial_user',
            'note': 'This is an initial note inserted upon launch.'
        }
        result = collection.insert_one(initial_document)
        print("Initial document inserted successfully with ID:", result.inserted_id)
    except Exception as e:
        print("Error inserting initial document:", e)

if __name__ == "__main__":
    # Insert initial document upon launch
    insert_initial_document(uri)
    
    # Run the Flask app
    app.run(debug=True)
