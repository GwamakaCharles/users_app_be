"""
This module contains the production environment variables.
"""

import os

from dotenv import load_dotenv

load_dotenv() # take environment variables from .env.

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'flask-insecure-7ppocbnx@w71dcuinn*t^_mzal(t@o01v3fee27g%rg18fc5d@'

DEBUG = False
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []
CSRF_TRUSTED_ORIGINS = ['https://'+ os.environ['WEBSITE_HOSTNAME']] if 'WEBSITE_HOSTNAME' in os.environ else []

# Configure Postgres database; the full username for PostgreSQL flexible server is
# username (not @sever-name).
DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DBUSER'],
    dbpass=os.environ['DBPASS'],
    dbhost=os.environ['DBHOST'] + ".postgres.database.azure.com",
    dbname=os.environ['DBNAME']
)


CACHE_REDIS_URL = 'redis://{redishost}:{redisport}/{redisdb}'.format(
    redishost=os.environ['CACHE_REDIS_HOST'],
    redisport=os.environ['CACHE_REDIS_PORT'],
    redisdb=os.environ['CACHE_REDIS_DB']
)

CACHE_TYPE="RedisCache"
CACHE_DEFAULT_TIMEOUT=300
