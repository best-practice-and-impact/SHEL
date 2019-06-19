from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField
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
    stakeholder_person = StringField('Name of Stakeholder', validators=[DataRequired()])
    organisation = SelectField('The government department',
    choices=[('DWP', 'DWP'), ('HMRC', 'The treasury!'), ('BEIS', 'BEIS'), ('DfS', 'DfS')], validators=[DataRequired()])
    stance = SelectField('What was there stance on quality',
    choices=[('1', 'Very Bad'), ('2', 'Bad'), ('3', 'Neutral'), ('3', 'Pretty Good'), ('5', 'Good!')])
    submit = SubmitField('Submit Data')
