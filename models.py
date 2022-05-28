from email.policy import default
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from App import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True, nullable = False)
    username = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(150), nullable = False)
    image_file = db.Column(db.String(30), nullable = False, default = 'defaut.jpg')


    def set_password(self, password):
        self.password = generate_password_hash(password, method="pbkdf2:sha256", salt_length = 32)


    def check_password(self, password):
        return check_password_hash(self.password, password)
