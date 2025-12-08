# Path: auth-service/app.py
from flask import Flask, request, jsonify
# ...
@app.route('/login', methods=['POST'])
def login():
    # ...
    # This block successfully logs the user in
    if data.get('username') == 'admin' and data.get('password') == 'admin123':
        return jsonify({"token": "fake-jwt-token-123", "message": "Success"}), 200
    
    # This block handles any incorrect login attempt
    # It sends the same 401 Unauthorized status regardless of whether the username 
    # or the password was incorrect.
    return jsonify({"message": "Invalid credentials"}), 401
# ...
