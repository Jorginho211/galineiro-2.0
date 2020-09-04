
class Development(object):
    DEBUG = True
    TESTING = True
    HOST = 'localhost'
    PORT = 5000


class Production(object):
    DEBUG = False
    TESTING = False
    HOST = '0.0.0.0'
    PORT = 5000


app_config = {
    'development': Development,
    'production': Production
}