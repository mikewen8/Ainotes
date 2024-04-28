from flask import request, jsonify

@app.route('/notes', methods=['GET'])
def get_notes():
    notes = mongo.db.notes.find()
    return jsonify([note for note in notes])

@app.route('/notes', methods=['POST'])
def create_note():
    note = request.json
    result = mongo.db.notes.insert_one(note)
    return jsonify({'id': str(result.inserted_id)}), 201

@app.route('/notes/<note_id>', methods=['PUT'])
def update_note(note_id):
    updated_data = request.json
    mongo.db.notes.update_one({'_id': note_id}, {'$set': updated_data})
    return jsonify({'message': 'Note Updated'})

@app.route('/notes/<note_id>', methods=['DELETE'])
def delete_note(note_id):
    mongo.db.notes.delete_one({'_id': note_id})
    return jsonify({'message': 'Note Deleted'}), 204

if __name__ == '__main__':
    app.run(debug=True)
