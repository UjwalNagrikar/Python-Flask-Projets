from flask import Flask, jsonify

app = Flask(__name__)

# Flask routing

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/hello')
def hello():
    return 'Hello, Flask!'

@app.route('/api/data')
def get_data():
    return jsonify({
        "name": "Flask API",
        "version": "1.0",
        "description": "A simple Flask API example"
    })

@app.route('/api/health')
def health():
    return jsonify({"status": "running"})

if __name__ == '__main__':
    app.run(debug=True)