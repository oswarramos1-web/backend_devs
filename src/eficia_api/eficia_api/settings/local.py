from .base import *

DEBUG = True

# Durante desarrollo permitimos hosts desde .env o localhost
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')
