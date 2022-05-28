from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:djdf2309865@localhost/accounts'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'