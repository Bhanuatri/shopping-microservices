from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Allow frontend to talk to this

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    # Hardcoded admin credentials
    if data.get('username') == 'admin' and data.get('password') == 'admin123':
        return jsonify({"token": "fake-jwt-token-123", "message": "Success"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
