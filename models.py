from datetime import datetime
from xml.dom import ValidationErr
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from App import db, app

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True, nullable = False)
    username = db.Column(db.String(50), unique = True, nullable = False)
    password = db.Column(db.String(150), nullable = False)
    image_file = db.Column(db.String(30), nullable = False, default = 'default.jpg')
    general_information = db.Column(db.String(200), nullable = True)


    def get_reset_token(self, expires_sec=300):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)


    def set_password(self, password):
        self.password = generate_password_hash(password, method="pbkdf2:sha256", salt_length = 32)


    def check_password(self, password):
        return check_password_hash(self.password, password)


    def past_passwrod_check(self, password):
        if(check_password_hash(self.password, password)):
            raise ValidationErr('Sorry, but your previous password is the same as your current one, please try again')


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