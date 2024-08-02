import pickle

from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={'/pipeline':{"origins":"http://localhost:8080"}})

with open("pipelines.pkl", "rb") as f:
    pipelines = pickle.load(f)

@app.route('/pipeline', methods=['POST'])
def post_request():
    result = None

    key = request.json["key"]

    if key in pipelines:
        pipeline = pickle.loads(pipelines[key])
    else:
        raise Exception("model not found!")
    
    encoder = pipeline.encoders[key]

    pipeline.transform(pipeline.prepare(data[:1]))

    return jsonify({'result': result})

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)