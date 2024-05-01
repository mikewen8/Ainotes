from doc_create import add_doc
from user_create import add_user
from pull import pull_doc, pull_user
id = pull_user()
doc =pull_doc()

new_doc=doc["_id"]
new_doc+=1
print(new_doc)

new_document = {
    "_id": new_doc,
    "userid":id["_id"],
    "Name": "Mike",
    "Note": "This is the very first note and it is a very very long note, it can be a very long long note maybe a full essay woth of notes I'm trying to see how much storage this will take for this super super long note",
}


new_id =id["_id"]
new_id +=1
print(new_id)
name = input(" input your name")
new_user ={
    "_id": new_id,
    "Name":name
}

def create_doc(new_document):
    add_doc(new_document)
def create_user(new_user):
    add_user(new_user)
    
create_doc(new_document)
create_user(new_user)