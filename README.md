# powerToFly
PowerToFly code challenge

**Stack**
- Flask
- Python3
- Redis
- SQLAlchemy
- Gunicorn
- Docker

**Endpoints**

There are two available endpoints:

`[GET] /users`
- List all users in the database using flask pagination. There is an optional arguments called page, you can add it to
the request to show different pages results, the default value of the parameter page is `1`.

`[POST] /users/filter`
- Brings users that fit the criteria. This endpoint expects a payload like the following:
```
{
    "name": "Maria",
    "country": "Brazil",
    "age": 23
}
```

The parameters above are all obligatory.
For the fields `name` and `country` that are Strings, the query used is SQL `LIKE` statement while the integer field
`age` matches using `==` statement.
