from flask_restful import Resource
from app import cache
from models import UserModel

class Users(Resource):
    @cache.cached(timeout=30)
    def get(self):
        return {'users' : [user.json() for user in UserModel.query.paginate().items]}

class User(Resource):
    @cache.cached(timeout=30)
    def get(self,name):
        user = UserModel.find_user_by_name(name)
        return user.json()
