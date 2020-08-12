from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap
from flask_datepicker import datepicker
from flask_mail import Mail
import os
import pymysql


app = Flask(__name__)
app.config.from_object(Config)

# def init_connection_engine():
#     db_config = {
#         "pool_size": 5,
#         "max_overflow": 2,
#         "pool_timeout": 30,
#         "pool_recycle": 1800,
#     }
#     if os.environ.get("DB_HOST"):
#         return init_tcp_connection_engine(db_config)
#     else:
#         return init_unix_conncetion_engine(db_config)

# def init_tcp_connection_engine(db_config):
#     db_user = os.environ["DB_USER"]
#     db_pass = os.environ["DB_PASS"]
#     db_name = os.environ["DB_NAME"]
#     db_host = os.environ["DB_HOST"]

#     host_args = db_host.split(":")
#     db_hostname, db_port = host_args[0], host_args[1]

#     pool =

db = SQLAlchemy(app)
#db = MySQLDatabase('shel-test', user='root', password='BestPractice', host='35.242.155.144', port=3306)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
bootstrap = Bootstrap(app)
datepicker = datepicker(app)
mail = Mail(app)


from app import routes, models
