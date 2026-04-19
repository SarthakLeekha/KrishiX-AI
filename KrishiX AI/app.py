import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from model_manager import manager

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_from_directory('..', 'index.html')

@app.route('/api/crop/recommend', methods=['POST'])
def recommend():
    data = request.json or {}
    result = manager.predict(data)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

