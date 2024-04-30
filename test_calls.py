from doc_create import add_doc
from user_create import add_user
from pull import pull_doc, pull_user
id = pull_user()
doc =pull_doc()

new_id =id["_id"]
new_id +=1
print(new_id)

new_doc=doc["_id"]
new_doc+=1
print(new_doc)

name = input(" input your name")

new_document = {
    "_id": new_doc,
    "userid":id["_id"],
    "Name": "Mike",
    "Note": "This is the very first note and it is a very very long note, it can be a very long long note maybe a full essay woth of notes I'm trying to see how much storage this will take for this super super long note",
}

new_user ={
    "_id": new_id,
    "Name":name
}

print (new_user)
add_doc(new_document)
add_user(new_user)