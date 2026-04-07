from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Dummy authentication logic
    if username == 'admin' and password == 'password':
        return jsonify({"message": "Login successful", "status": "success"})
    else:
        return jsonify({"message": "Invalid credentials", "status": "error"}), 401

if __name__ == "__main__":
    app.run(debug=True)