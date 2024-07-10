# app.py

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/submit', methods=['POST'])
def submit_data():
    data = request.get_json()
    name = data['name']
    email = data['email']
    food = data['food']
    print(f"Received data: {name}, {email}, {food}")
    return jsonify({'name': name, 'email': email, 'food': food})

if __name__ == '__main__':
    app.run(debug=True)