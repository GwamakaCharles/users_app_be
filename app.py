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

r = redis.Redis(host='cache', port=6379, db=0)
cache = Cache(app)

class Users(Resource):
    def get(self):
        return {'users' : [user.json() for user in UserModel.query.paginate().items]}

class User(Resource):
    def get(self,name):
        user = UserModel.find_user_by_name(name)
        return user.json()


class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    country = db.Column(db.String(50))

    # def __init__(self, id, name, age, country):
    #     self.id = id
    #     self.name = name
    #     self.age = age
    #     self.country = country

    def json(self):
        return {'name': self.name, 'age':self.age, 'country':self.country}
    
    @classmethod
    def find_user_by_name(cls,name): 
       return cls.query.filter_by(name=name).first_or_404()


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/', methods=['GET'])
def home():
    return f'Hello! Welcome to my power to fly code challenge. The endpoints available are /users and /user/<string:name>'

api.add_resource(Users, '/users')
api.add_resource(User, '/user/<string:name>')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
