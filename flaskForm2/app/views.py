from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import NewForm
from models import User, ROLE_USER, ROLE_ADMIN
from datetime import datetime

@app.before_request
def before_request():
    g.user = current_user


@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
    return render_template('login.html', 
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS'])

@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('enter'))

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('enter'))

@app.route('/enter', methods = ['GET', 'POST'])
def enter():
    form = NewForm()
    if form.validate_on_submit():
        g.user.latitude = form.latitude.data
        g.user.longitude = form.longitude.data
        g.user.phone = form.phone.data
        fo = open("info.txt", 'w')
        fo.write(g.user.latitude + "\n")
        fo.write(g.user.longitude + "\n")
        fo.write(g.user.phone + "\n")
        fo.close()
        db.session.add(g.user)
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('enter'))
    else:
        form.longitude.data = g.user.longitude
        form.latitude.data = g.user.latitude
        form.phone.data = g.user.phone
    return render_template('enter.html',
        form = form)
