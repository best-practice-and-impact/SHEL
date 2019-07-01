from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField, SelectMultipleField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User, Logstakeholder


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class Stakeholderlog(FlaskForm):
    date = DateField('Date, example 17/02/2019', format='%d/%m/%Y', validators=[DataRequired()])
    stakeholder_person = StringField('Stakeholder name', validators=[DataRequired()])
    organisation = SelectField('Organisation',
    choices=[('DWP', 'DWP'), ('HMRC', 'The treasury!'), ('BEIS', 'BEIS'), ('DfS', 'DfS')], validators=[DataRequired()])
    stance = SelectField('Engagement with quality',
    choices=[('1', 'Resistant'), ('2', 'Cautious'), ('3', 'Neutral'), ('4', 'Engaged'), ('5', 'Champion')])
    meeting = SelectField('Meeting format',
    choices=[ ('Conference', 'Conference'), ('Informal', 'Informal'), ('One to one', 'One to one'), ('Roundtable', 'Roundtable'), ('Seminar', 'Seminar'), ('Workshop', 'Workshop'),])
    keypoints = StringField('Key points from meeting', validators=[DataRequired()])
    bpier = SelectMultipleField('BPI attendee(s)',
    choices=[('James', 'James'), ('Jack', 'Jack'), ('Rebecca', 'Rebecca'), ('Josh', 'Josh'), ('Catrin', 'Catrin'), ('Louise', 'Louise')] )
    submit = SubmitField('Submit Data')

class FilterTable(FlaskForm):
    department = SelectMultipleField('Organisation',
    choices=[('DWP', 'DWP'), ('HMRC', 'The treasury!'), ('BEIS', 'BEIS'), ('DfS', 'DfS')])
    stance = SelectField('Engagement with quality',
    choices=[("0", "Select Option"),('1', 'Resistant'), ('2', 'Cautious'), ('3', 'Neutral'), ('4', 'Engaged'), ('5', 'Champion')])
    submit = SubmitField("Submit Filter")
