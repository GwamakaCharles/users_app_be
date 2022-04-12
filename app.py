from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder
from flask_restful import Resource, Api
from flask_wtf.csrf import CSRFProtect
from resources import Users, User
import redis
import os
from flask_caching import Cache

# Creates an instance of the Flask class called 'app'
app = Flask(__name__)
csrf = CSRFProtect(app)

# WEBSITE_HOSTNAME exists only in production environment
if not 'WEBSITE_HOSTNAME' in os.environ:
   # local development, where we'll use environment variables
   print("Loading config.development and environment variables from .env file.")
   app.config.from_object('env_variables.development')
else:
   # production
   print("Loading config.production.")
   app.config.from_object('env_variables.production')

app.config.update(
    SQLALCHEMY_DATABASE_URI=app.config.get('DATABASE_URI'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

# Create an instance of the Api class for the app to create the routes
api = Api(app)

# Initialize the database connection
db = SQLAlchemy(app)

# tell Flask to use the above defined config
app.config.from_object('env_variables.development')
cache = Cache(app)

@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/', methods=['GET'])
def home():
    return f"The endpoints available are /users and /user/<name>. For example, /users will return all the users and /user/<name> will return the user with the given name."


# endpoint to retrieve all users
api.add_resource(Users, '/users')

# endpoint to retrieve a user by name
api.add_resource(User, '/user/<string:name>')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
