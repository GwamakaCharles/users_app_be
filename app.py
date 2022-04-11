from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder
import redis
from flask_caching import Cache

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://root:postgres@database:5432/users_app_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

r = redis.Redis(host='cache', port=6379, db=0)
cache = Cache(app)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    country = db.Column(db.String(50))

    def __init__(self, id, name, age, country):
        self.id = id
        self.name = name
        self.age = age
        self.country = country

    def json(self):
        return {'name': self.name, 'age':self.age, 'country':self.country}


seeder = FlaskSeeder()
seeder.init_app(app, db)
db.create_all()
db.session.commit()


@app.route('/', methods=['GET'])
def home():
    return f'Hello! Welcome to my power to fly code challenge. The endpoints available are /users and /users/filter'


@app.route('/users', methods=['GET'], defaults={"page": 1})
@app.route('/<int:page>', methods=['GET'])
@cache.cached(timeout=30, query_string=True)
def get_users(page):
    ROWS_PER_PAGE = 100 #Show 100 users per page

    page = page

    users = Users.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    paginated_users = users.items

    all_users = [{
        'name': user.name,
        'age': user.age,
        'country': user.country
    } for user in paginated_users]

    return jsonify({
        'success': True,
        'users': all_users,
        'count': len(paginated_users)
    })


@app.route('/users/filter', methods=['POST'])
@cache.cached(timeout=30, query_string=True)
def get_users_filtered():
    ROWS_PER_PAGE = 100

    page = request.args.get('page', 1, type=int)
    filters = request.get_json()

    name = None
    age = None
    country = None

    if filters:
        if 'name' in filters:
            name = filters['name']

        if 'age' in filters:
            age = filters['age']

        if 'country' in filters:
            country = filters['country']

    users = Users.query.filter(
        Users.name.ilike(name),
        Users.country.ilike(country),
        Users.age == age
    ).paginate(page=page, per_page=ROWS_PER_PAGE)

    paginated_users = users.items

    result = [{
        'name': user.name,
        'age': user.age,
        'country': user.country
    } for user in paginated_users]

    return jsonify({
        'success': True,
        'users': result,
        'count': len(paginated_users)
    })


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
