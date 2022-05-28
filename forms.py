from flask_wtf import FlaskForm
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


class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired(), Email()], render_kw = {"placeholder":"Email"})

    password = PasswordField(validators=[DataRequired()], render_kw = {"placeholder":"Password"})

    remember = BooleanField('Rememer Me' ,validators=[DataRequired()])
    
    submit = SubmitField("Login")