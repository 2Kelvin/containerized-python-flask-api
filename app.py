from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from the containerized Flask API!'

if __name__ == '__main__':
    # used 0.0.0.0 so it's accessible outside the container
    app.run(host='0.0.0.0', port=5000)