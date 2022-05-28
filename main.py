from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user, current_user, logout_user, login_required
from models import User
from forms import LoginForm,RegisterForm
from App import app, db, login_manager


@app.route("/")
def home():
    return render_template('index.html')


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route("/login", methods = ['GET', 'POST'])
def login():
    form = LoginForm()

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
        return redirect(url_for('store'))

    if form.validate_on_submit():
        new_user = User(email = form.email.data, username = form.username.data)
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('reg.html', form_reg = form)


@app.route("/shop")
def shop():
    return render_template('store.html')


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/account")
@login_required
def account():
    return render_template('store.html', title = 'Account')

if __name__ == '__main__':
    app.run(debug=True)