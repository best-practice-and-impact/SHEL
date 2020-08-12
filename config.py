import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    #    'sqlite:///' + os.path.join(basedir, 'app.db')
    #SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:BestPractice@35.242.155.144:3306/shel-test"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['jack.sim.test@gmail.com']
    POSTS_PER_PAGE = 25
    CLOUDSQL_USER = os.environ.get('DB_USER')
    CLOUDSQL_PASSWORD = os.environ.get('DB_PASS')
    CLOUDSQL_DATABASE = os.environ.get('DB_NAME')
    CLOUDSQL_CONNECTION_NAME = os.environ.get('CLOUD_SQL_CONNECTION_NAME')
    LOCAL_SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://{nam}:{pas}@127.0.0.1:3306/{dbn}').format (
        nam=CLOUDSQL_USER,
        pas=CLOUDSQL_PASSWORD,
        dbn=CLOUDSQL_DATABASE,
    )

    LIVE_SQLALCHEMY_DATABASE_URI = (
        'mysql+pymysql://{nam}:{pas}@localhost/{dbn}?unix_socket=/cloudsql/{con}').format (
        nam=CLOUDSQL_USER,
        pas=CLOUDSQL_PASSWORD,
        dbn=CLOUDSQL_DATABASE,
        con=CLOUDSQL_CONNECTION_NAME,
    )

    if os.environ.get ('GAE_INSTANCE'):
        SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI
    else:
        SQLALCHEMY_DATABASE_URI = LOCAL_SQLALCHEMY_DATABASE_URI
