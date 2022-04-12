from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv() # take environment variables from .env.


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DBUSER'],
    dbpass=os.environ['DBPASS'],
    dbhost=os.environ['DBHOST'],
    dbname=os.environ['DBNAME']
)

CACHE_REDIS_URL = 'redis://{redishost}:{redisport}/{redisdb}'.format(
    redishost=os.environ['CACHE_REDIS_HOST'],
    redisport=os.environ['CACHE_REDIS_PORT'],
    redisdb=os.environ['CACHE_REDIS_DB']
)

CACHE_TYPE=RedisCache
CACHE_DEFAULT_TIMEOUT=300


TIME_ZONE = 'UTC'

STATICFILES_DIRS = (str(BASE_DIR.joinpath('static')),)
STATIC_URL = 'static/'