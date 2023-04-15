from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/convert-to-json', methods=['POST'])
def convert_to_json():
    data = request.get_json()
    name = data['name']
    nationality = data['nationality']
    bj = data['bj']
    a = data['a']
    f = data['f']
    score = data['score']
    
    # Create a dictionary from the input data
    result = {
        "name": name,
        "nationality": nationality,
        "bj": bj,
        "a": a,
        "f": f,
        "score": score
    }
    
    # Convert dictionary to JSON string
    result_json = json.dumps(result)
    
    return result_json, 200

if __name__ == '__main__':
    app.run()