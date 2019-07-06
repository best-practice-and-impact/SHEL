from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.String(10))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Logstakeholder(db.Model):
    test = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    stakeholder_person = db.Column(db.String(120), index=True)
    organisation = db.Column(db.String(120), index=True)
    stance = db.Column(db.Integer)
    user_id = db.Column(db.String(120), db.ForeignKey('user.username'))
    keypoints = db.Column(db.String(120), index=True)
    bpier = db.Column(db.String(120))
    meeting = db.Column(db.String(120))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)
