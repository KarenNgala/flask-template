import os

class Config:
    ''' general config parent class '''
    API_KEY = os.environ.get('API_KEY')
    # API_BSE_URL
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # UPLOADED_PHOTOS_DEST = 'app/static/photos'
    # email configs -> MAIL_SERVER, MAIL_PORT, MAIL_USE_TLS, MAIL_USERNAME, MAIL_PASSWORD
    # simplemde configs -> SIMPLEMDE_JS_IIFE, SIMPLEMDE_USE_CON


class ProductionConfig(Config):
    ''' Production config child class. Args: Config -> parent config class '''
    pass

# TestConfig class here
# SQLALCHEMY_DATABASE_URI (env var) -> Dev, Test & Prod 


class DevelopmentConfig(Config):
    ''' Development config child class. Args: Config -> parent config class '''
    DEBUG=True


config_options = {
    'dev': DevelopmentConfig,
    'prod': ProductionConfig
}