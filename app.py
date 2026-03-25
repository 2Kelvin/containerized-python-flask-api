from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        "message": "Hello from the containerized Flask API!",
        "status": "success"
    })

if __name__ == '__main__':
    # We use 0.0.0.0 so it's accessible outside the container
    app.run(host='0.0.0.0', port=5000)