from flask import Flask, jsonify, request

# Dummy function TRANS.get_transcript
def get_transcript(id, preserve_formatting=True):
    # Dummy data
    return [
        {'text': 'Hey there', 'start': 7.58, 'duration': 6.13},
        {'text': 'how are you', 'start': 14.08, 'duration': 7.58}
    ]

app = Flask(__name__)

@app.route('/api/extract-transcript', methods=['GET'])
def extract_transcript():
    # Extract the 'id' parameter from the query string
    id_value = request.args.get('id')

    if id_value:
        # Call TRANS.get_transcript function to get the transcript
        result = get_transcript(id_value, preserve_formatting=True)
        
        # Convert the transcript to JSON format
        return jsonify(result)
    else:
        return jsonify({"error": "'id' parameter not found in URL"}), 400

if __name__ == "__main__":
    app.run(debug=True)
