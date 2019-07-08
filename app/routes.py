from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, Stakeholderlog, FilterTable, PostForm
from app.models import User, Logstakeholder, Post
from flask_datepicker import datepicker


@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Home')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout1', methods=['GET', 'POST'])
@login_required
def logout1():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, is_admin = "False")
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/Stakeholder_log', methods=['GET', 'POST'])
@login_required
def Stakeholder_log():
    form = Stakeholderlog()
    if form.validate_on_submit():
            log = Logstakeholder(date=form.date.data, stakeholder_person=form.stakeholder_person.data, user_id=current_user.username,
            organisation=form.organisation.data, stance=form.stance.data, meeting=form.meeting.data, keypoints=form.keypoints.data, bpier=" , ".join(form.bpier.data) )
            db.session.add(log)
            db.session.commit()
            flash('Data has been submitted!')
            return redirect(url_for('index'))
    return render_template('stakeholder_log.html', title='Log Form', form=form)

@app.route('/display', methods=["GET","POST"])
@login_required
def display():
    if current_user.is_admin == "True":
        form = FilterTable()
        department = []
        stance = 0
        if form.validate_on_submit():
            department = form.department.data
            stance = int(form.stance.data)
        else:
            pass

        if len(department) == 0:
            department = ["DWP", "HMRC", "BEIS", "DfS"]
        else:
            pass
        people = User.query.all()
        shel = Logstakeholder.query.all()
        return render_template('display.html', form=form, people=people, shel=shel, department=department, stance=stance)
    else:
        flash("You don't have permission!")
        return redirect(url_for('index'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if current_user.is_admin == "True":
        form = PostForm()
        if form.validate_on_submit():
            post = Post(body=form.post.data, author=current_user)
            db.session.add(post)
            db.session.commit()
            flash("Your post is now live!")
            return redirect(url_for('admin'))
        return render_template('admin.html', title='Admin Page', form=form)
    else:
        flask("You are not an admin, you don't have permission to view this page")
        return redirect(url_for('index'))

@app.route('/register_admin', methods=['GET', 'POST'])
def register_admin():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, is_admin = "True")
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered admin!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register Admin User', form=form)
