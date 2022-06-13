from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from models import User
from wtforms import StringField, PasswordField, SubmitField, BooleanField
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