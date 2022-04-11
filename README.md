# powerToFly
PowerToFly code challenge

**Stack**
- Flask
- Postgresql
- Redis
- Docker

**API Endpoints**
Read the api.yaml first to understand how the API endpoints are used.

## There are two available endpoints:

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

