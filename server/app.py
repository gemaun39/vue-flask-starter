#!env/bin/python
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/api/v1.0/hello', methods=['GET'])
def get_tasks():
    return jsonify({'message': "Hello, client!"})

if __name__ == '__main__':
    app.run(debug=True)