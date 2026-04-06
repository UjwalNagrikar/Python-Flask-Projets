from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    return {"message": "Data received", "data": data}

if __name__ == "__main__":
    app.run(debug=True)