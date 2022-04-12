# powerToFly

PowerToFly code challenge

**Stack**

- Flask
- Postgresql
- Redis
- Docker

# SETUP

## Docker

Clone this repo to your local machine

```
git clone https://github.com/GwamakaCharles/users_app_be/
```

cd users_app_be

```
docker-compose up
```

The app will be running on port 5000 so you can access it at http://localhost:5000

Connect to the database using the following command

```
docker exec -it users_app_db psql -U postgres
```

Or use the [Postico](https://eggerapps.at/postico/) utility to connect to the database using the database credentials available in the docker-compose.yml file

Fill the users table with dummy data using the following command

```sql
insert into users (
	name, age, country)
select
	left(md5(i::text), 10),
	(floor(random() * 100 + 1)::int),
	left(md5(random()::text), 10)
from generate_series(1,1000000) s(i);
```

**API Endpoints**

Read the _api.yaml_ file first to understand how the API endpoints are used.

## There are two endpoints available:

`[GET] /users`

- Returns a list of all users.

for filtering the users, you can use the following query parameters:
`[GET] /user/<name>`

- Brings user with the given name.
  for example: `/user/john` will bring the user with name `john`.

for pagination, you can use the following parameters:

- page: the page number, default value is 1
- per_page: the number of results per page, default value is 20
  for example:
  `[GET] /users?page=2&per_page=10`
- Brings the second page of 10 users.
