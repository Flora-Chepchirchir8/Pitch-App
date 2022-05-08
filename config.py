import os

class Config:

    SECRET_KEY = 'f2GDBACdGn5ZGx$A!gC[:+*/b.JS?('
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jaysafu@localhost/pitcheslist'
    UPLOADED_PHOTOS_DEST ='app/static/photos'

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SUBJECT_PREFIX = 'LORA PITCH-APP!'
    SENDER_EMAIL = 'florachirry80@gmail.com'

    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    class ProdConfig(Config):
     uri = os.getenv('DATABASE_URL')
     if uri and uri.startswith('postgres://'):
        uri = uri.replace('postgres://', 'postgresql://', 1)
        
        SQLALCHEMY_DATABASE_URI=uri
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):

#   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jaysafu@localhost/pitches_test'
  pass

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:jaysafu@localhost/pitcheslist'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}