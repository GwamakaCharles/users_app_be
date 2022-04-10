from flask_seeder import Seeder, Faker, generator
from flask_seeder.generator import Generator

from app import Users


class Country(Generator):
    def __init__(self, **kwargs):
        super(Country, self).__init__(**kwargs)
        self._lines = None

    def generate(self):
        if self._lines is None:
            self._lines = open('seeds/countries.txt', 'r').readlines()

        country = self.rnd.choice(self._lines).strip()

        return country


class UserSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 10

    def run(self):

        faker = Faker(
            cls=Users,
            init={
                "id": generator.Sequence(),
                "name": generator.Name(),
                "age": generator.Integer(start=20, end=100),
                "country": Country()
            }
        )

        for user in faker.create(1000000):
            print("Adding user: %s" % user)
            self.db.session.add(user)
