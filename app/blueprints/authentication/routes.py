from app import db
from flask import request, render_template, flash, redirect, url_for
from .import bp as authentication
from app.blueprints.authentication.models import User
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse

@authentication.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        r = request.form
        if r.get('confirm_password') == r.get('password'):
            data = {
                'first_name': r.get('first_name'),
                'last_name': r.get('last_name'),
                'email': r.get('email'),
                'password': r.get('password'),
            }
            u = User(first_name=data['first_name'], last_name=data['last_name'], email=data['email'], password=data['password'])
            u.hash_password(u.password)
            db.session.add(u)
            db.session.commit()
            flash("You have registered successfully", 'primary')
            return redirect(url_for('authentication.login'))
    return render_template('register.html')

@authentication.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        r = request.form
        user = User.query.filter_by(email=r.get('email')).first()
        if user is None or not user.check_password(r.get('password')):
            flash("You have used either an incorrect email or password", 'danger')
            return redirect(url_for('authentication.login'))
        login_user(user, remember=r.get('remember_me'))
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        flash("You have logged in successfully", 'success')
        return redirect(next_page)
    return render_template('login.html')

@authentication.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out", 'info')
    return redirect(url_for('authentication.login'))