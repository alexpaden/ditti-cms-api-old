from flask import Flask, jsonify, request
from ditti_web.controllers.follow import get_followers
from ditti_web.models import FollowTracker, TrackerManager, Trackee, ProfileTracker
from ditti_web.config import Config
from ditti_web.database import init_app

app = Flask(__name__)
app.config.from_object(Config)

init_app(app)

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
