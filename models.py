from app import db, cache

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