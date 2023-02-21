# Import necessary modules
from ditti_web.controllers.follow import get_followers
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# Define a simple "hello world" route
@app.route('/')
def index():
    result = get_followers()
    return result

# Define a route that takes a query parameter
@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name:
        return f'Hello, {name}!'
    else:
        return 'Hello, stranger!'

# Define a route that returns JSON data
@app.route('/data')
def data():
    return jsonify({
        'name': 'John',
        'age': 30,
        'email': 'john@example.com'
    })