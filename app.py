from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder
from flask_restful import Resource, Api
import redis
from flask_caching import Cache

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://root:postgres@database:5432/users_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)

# Configure Redis cache
# r = redis.Redis(host='cache', port=6379, db=0)
config = {
    "CACHE_TYPE": "RedisCache",  # Set up Redis as the cache
    "CACHE_REDIS_HOST": "redis",  # Set the Redis host
    "CACHE_REDIS_PORT": 6379, # Set the Redis port
    "CACHE_REDIS_DB": 0, # Set the Redis DB
    "CACHE_REDIS_URL": "redis://redis:6379/0", # Set the Redis URL
    "CACHE_DEFAULT_TIMEOUT": 300 # Set the default cache timeout
}
# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)

class Users(Resource):
    @cache.cached(timeout=30)
    def get(self):
        return {'users' : [user.json() for user in UserModel.query.paginate().items]}

class User(Resource):
    @cache.cached(timeout=30)
    def get(self,name):
        user = UserModel.find_user_by_name(name)
        return user.json()


class UserModel(db.Model):
    """
    Create a new user model with the given name, age and country
    """
    __tablename__ = 'users' # table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    country = db.Column(db.String(50))

    def json(self):
        return {'name': self.name, 'age':self.age, 'country':self.country}
    
    @classmethod
    @cache.cached(timeout=30)
    def find_user_by_name(cls,name): 
       return cls.query.filter_by(name=name).first_or_404()


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/', methods=['GET'])
def home():
    return f'Hello! Welcome to my power to fly code challenge. The endpoints available are /users and /user/<string:name>'

# endpoint to retrieve all users
api.add_resource(Users, '/users')

# endpoint to retrieve a user by name
api.add_resource(User, '/user/<string:name>')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
