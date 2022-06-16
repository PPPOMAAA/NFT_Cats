from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from models import User, NFT
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegisterForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email(message='Почта уже зарегистрированна',
    check_deliverability= True)], render_kw={"placeholder":"Email"})

    username = StringField(validators=[DataRequired(), Length(
        min = 5)], render_kw={"placeholder":"Username"})

    password = PasswordField(validators=[DataRequired(), Length(
        min = 8)], render_kw={"placeholder":"Password"})

    confirm = PasswordField(validators=[DataRequired(),EqualTo('password',
        message='Passwords do not match, please try again'),Length(min = 8)], render_kw = {"placeholder":"Confirm Password"})

    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationErr('That username is taken. Please choose a different one.')

    
    def vallidate_email(self, email):
        current_email = User.quey.filter_by(email = email.data).first()
        if current_email:
            raise ValidationErr('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()], render_kw = {"placeholder":"Email"})

    password = PasswordField(validators=[DataRequired()], render_kw = {"placeholder":"Password"})

    remember = BooleanField('Rememer Me' ,validators=[DataRequired()])
    
    submit = SubmitField("Login")


class UpdateAccountForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email(message='Почта уже зарегистрированна',
    check_deliverability= True)], render_kw={"placeholder":"Email"})

    picture = FileField(validators=[FileAllowed(['jpg', 'png'])])

    username = StringField(validators=[DataRequired(), Length(
        min = 5)], render_kw={"placeholder":"Username"})

    name = StringField(validators=[DataRequired()], render_kw={"placeholder":"Your Name"})

    general_information = StringField(validators=[DataRequired()], render_kw={"placeholder":"Personal Information"})
        
    submit = SubmitField("Update")
    

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username = username.data).first()
            if user:
                raise ValidationErr('That username is taken. Please choose a different one.')
    

    def validate_email(self, email):
        if email.data != current_user.email:
            current_email = User.query.filter_by(email = email.data).first()
            if current_email:
                raise ValidationErr('That email is taken. Please choose a different one.')


class NftForm(FlaskForm):
    picture = FileField(validators = [FileAllowed(['jpg', 'png'])])
    
    name = StringField(validators = [DataRequired()], render_kw = {"placeholder":"Name NFT"})

    description = StringField(validators = [DataRequired()], render_kw = {"placeholder":"Information about NFT"})

    price = FloatField(validators = [DataRequired()])

    submit = SubmitField("Create")


    def validate_name(self,name):
        name = NFT.query.filter_by(name = name.data).first()
        if name:
            raise ValidationErr('NFT with this name has already been created, please come up with a new name')