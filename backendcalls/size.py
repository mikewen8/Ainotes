
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Mike:Mikedev88@studygroup.zvgkeux.mongodb.net/?retryWrites=true&w=majority&appName=Studygroup"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['Studygroup']

# Get database stats
db_stats = db.command("dbstats")

# Print the size of the database in bytes and in megabytes
print("Database size in bytes:", db_stats['dataSize'])
print("Database size in megabytes:", db_stats['dataSize'] / (1024 * 1024))