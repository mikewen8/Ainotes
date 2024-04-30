from doc_create import add_doc
from pull import pull_doc, pull_user
id = pull_user()

new_id =id["_id"]
new_id +=1
print(new_id)
document = {
    "_id": new_id,
    "Name": "Mike",
    "Note": "This is the very first note and it is a very very long note, it can be a very long long note maybe a full essay woth of notes I'm trying to see how much storage this will take for this super super long note",
}

#add_doc(document)