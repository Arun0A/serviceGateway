from flask import Flask, request, jsonify
import requests

# Initialize Flask app
app = Flask(__name__)

# Mock service URLs (you can replace these with actual service URLs)
SERVICE_1_URL = "http://mock-service1.local"
SERVICE_2_URL = "http://mock-service2.local"

# Logging middleware
@app.before_request
def log_request():
    print(f"Received {request.method} request at {request.path}")

# Route to Service 1
@app.route('/service1', methods=['GET', 'POST'])
def route_to_service1():
    if request.method == 'GET':
        response = requests.get(SERVICE_1_URL, params=request.args)
    else:
        response = requests.post(SERVICE_1_URL, json=request.json)
    return jsonify(response.json()), response.status_code

# Route to Service 2
@app.route('/service2', methods=['GET', 'POST'])
def route_to_service2():
    if request.method == 'GET':
        response = requests.get(SERVICE_2_URL, params=request.args)
    else:
        response = requests.post(SERVICE_2_URL, json=request.json)
    return jsonify(response.json()), response.status_code

# Run the API Gateway
if __name__ == '__main__':
    app.run(debug=True, port=5000)
