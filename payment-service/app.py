from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/pay', methods=['POST'])
def pay():
    # Simulate payment processing
    return jsonify({"status": "Payment Successful", "transaction_id": "TXN_9999"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
