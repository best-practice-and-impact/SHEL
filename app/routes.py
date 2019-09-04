from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, Stakeholderlog, FilterTable, PostForm, ResetPasswordRequestForm, ResetPasswordForm, RequestUserForm, SetPasswordForm, ChooseGraph
from app.models import User, Logstakeholder, Post
from flask_datepicker import datepicker
from app.email import send_password_reset_email, send_registration_request_email
import json
#import matplotlib.pyplot as plt
#import seaborn as sns
#from flask import Response
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
#from matplotlib.figure import Figure


@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = Post.query.all()
    event = Post.query.first()
    return render_template('index.html', title='Home', posts=posts, event=event)


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
        #user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('complete_registration_request'))
    return render_template('register.html', title='Register', form=form)


@app.route('/Stakeholder_log', methods=['GET', 'POST'])
@login_required
def Stakeholder_log():
    form = Stakeholderlog()
    if form.validate_on_submit():
            log = Logstakeholder(date=form.date.data, stakeholder_person=form.stakeholder_person.data, user_id=current_user.username,
            organisation=form.organisation.data, stance=form.stance.data, meeting=form.meeting.data, keypoints=form.keypoints.data, bpier=", ".join(form.bpier.data) )
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
            department = ['BEIS', 'Cabinet Office', 'CaCHE', 'DCMS', 'DfE', 'DfT', 'DHSC', 'DWP', 'HMRC', 'Home Office', 'MHCLG', 'MOD', 'MoJ',
            'NWIS', 'ONS', 'OSR', 'Welsh Gov', 'Other Government Department', 'Other University', 'Other Private Institution']
        else:
            pass
        shel = Logstakeholder.query.all()
        return render_template('display.html', form=form, shel=shel, department=department, stance=stance)
    else:
        flash("You don't have permission!")
        return redirect(url_for('index'))

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    if current_user.is_admin == "True":
        people = User.query.all()
        form = PostForm()
        if form.validate_on_submit():
            post = Post(body = form.post.data, location = form.location.data, date = form.date.data, author=current_user)
            db.session.add(post)
            db.session.commit()
            flash("Your post is now live!")
            return redirect(url_for('admin'))
        return render_template('admin.html', title='Admin Page', form=form, people=people)
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
        #user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered admin!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register Admin User', form=form)

@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html',
                           title='Reset Password', form=form)

@app.route('/complete_registration_request', methods=['GET', 'POST'])
def complete_registration_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RequestUserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_registration_request_email(user)
        flash('Check your email for the instructions to register your account')
        return redirect(url_for('login'))
    return render_template('complete_registration_request.html',
                           title='Complete Registration', form=form)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form)


@app.route('/register_new_user/<token>', methods=['GET', 'POST'])
def register_new_user(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = SetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been set.')
        return redirect(url_for('login'))
    return render_template('register_new_user.html', form=form)

@app.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    shel_data = Logstakeholder.query.all()
    dept_breakdown = {}

    for log in shel_data:
        if log.organisation in dept_breakdown:
            dept_breakdown[str(log.organisation)] += 1
        else:
            dept_breakdown[str(log.organisation)] = 1
    # Generate the counts to make plots from
    out_dictionary = {"dept":{}, "stance":{"1":0,"2":0,"3":0,"4":0,"5":0}, "meet_type":{}}

    pie_data_meet_type = {'Conference':{"count":0, "color":"red", "label":"Conference"},
                        "Informal":{"count":0, "color":"blue", "label":"Informal"},
                        "One to one": {"count":0, "color":"green", "label":"One to one"},
                        "Roundtable":{"count":0, "color":"yellow", "label":"Roundtable"},
                        "Seminar":{"count":0, "color":"pink", "label":"Seminar"},
                        "Workshop":{"count":0, "color":"black", "label":"Workshop"}}

    for log in shel_data:
        if log.organisation in out_dictionary['dept']:
            out_dictionary['dept'][str(log.organisation)] += 1
        else:
            out_dictionary['dept'][str(log.organisation)] = 1

        out_dictionary['stance'][str(log.stance)] += 1

        if log.meeting in out_dictionary['meet_type']:
            out_dictionary['meet_type'][str(log.meeting)] += 1
        else:
            out_dictionary['meet_type'][str(log.meeting)] = 1

        pie_data_meet_type[log.meeting]["count"] += 1
    # Import the form to select the graph
    form = ChooseGraph()
    graph_output = "dept"
    if form.validate_on_submit():
        graph_output = form.graph_type.data
    else:
        pass

    return render_template('dashboard.html', title='Dashboard', data=json.dumps(dept_breakdown), more_data=json.dumps(out_dictionary), form=form, graph_output=graph_output, pie_chart_data=json.dumps(pie_data_meet_type))
