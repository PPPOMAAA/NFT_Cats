from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user, current_user, logout_user, login_required
from models import User
import secrets
import os
from forms import LoginForm, RegisterForm, UpdateAccountForm
from App import app, db, login_manager


@app.route("/")
def home():
    return render_template('index.html')


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route("/login", methods = ['POST', 'GET'])
def login():
    form = LoginForm()
    print(form.validate_on_submit())

    if current_user.is_authenticated:
        return redirect(url_for('shop'))

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next = request.args.get("next")
            return redirect(next or url_for('shop'))
        flash('Invalid email address or Password.')
    return render_template('login.html', form_login = form)


@app.route("/register", methods = ['POST', 'GET'])
def register():
    form = RegisterForm()

    if current_user.is_authenticated:
        return redirect(url_for('shop'))

    if form.validate_on_submit():
        new_user = User(email = form.email.data, username = form.username.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('reg.html', title = 'Register',form_reg = form)


@app.route("/shop")
def shop():
    return render_template('store.html')


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + file_ext
    picture_path = os.path.join(app.root_path, 'static', picture_fn)
    form_picture.save(picture_path)

    return picture_fn


@app.route("/settings", methods = ['POST', 'GET'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data: 
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.name = form.name.data
        current_user.general_information = form.general_information.data
        db.session.commit()
        flash('your account has been update!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.name.data = current_user.name
        form.general_information.data = current_user.general_information
    image_file = url_for('static', filename = '' + current_user.image_file )
    return render_template('settings.html', title = 'Account', image_file = image_file, form_account = form)

if __name__ == '__main__':
    app.run(debug=True)