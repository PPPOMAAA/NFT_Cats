from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from App import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True, nullable = False)
    username = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(150), nullable = False)
    image_file = db.Column(db.String(30), nullable = False, default = 'default.jpg')
    general_information = db.Column(db.String(200), nullable = True)


    def set_password(self, password):
        self.password = generate_password_hash(password, method="pbkdf2:sha256", salt_length = 32)


    def check_password(self, password):
        return check_password_hash(self.password, password)


class NFT(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image_file = db.Column(db.String(50), nullable = True)
    name = db.Column(db.String(50), nullable = False, unique = True)
    description = db.Column(db.Text, nullable = False)
    price = db.Column(db.Float(30), nullable = False)
    date_creator = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    owner_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    creator = db.relationship("User", foreign_keys = [creator_id], backref = 'creator', lazy = True)
    owner = db.relationship("User", foreign_keys = [owner_id], backref = 'owner', lazy = True)