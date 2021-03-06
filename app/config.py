import os


class Config(object):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DEBUG = False
    TESTING =   False
    SECRET_KEY = 'This is an INSECURE secret!! DO NOT use this in production!!'
    SESSION_COOKIE_SECURE = True
    BOOTSTRAP_BOOTSWATCH_THEME = 'Simplex'
    db_dir = "database/db.sqlite"
    DB_DIR = os.getenv('DB_DIR', 'database')
    LOG_DIR = os.path.join(BASE_DIR, '../logs')
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, '..', DB_DIR, "db.sqlite")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', BASE_DIR + '/uploads')


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SESSION_COOKIE_SECURE = False
    DEBUG = True
