from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, SelectField, SelectMultipleField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User, Logstakeholder


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

#===============================================================================================================

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    #password = PasswordField('Password', validators=[DataRequired()])
    #password2 = PasswordField(
    #    'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
        elif not email.data.endswith("@ons.gov.uk"):
            raise ValidationError("Email address is invalid")

#===============================================================================================================

class PostForm(FlaskForm):
    post = TextAreaField('Home Page Events', validators=[DataRequired(), Length(min=1, max=150)])
    location = StringField("Event Location", validators=[DataRequired()])
    date = StringField('Date, example 17/02/2019', id='datepick', validators=[DataRequired()])
    submit = SubmitField('Post')

#===============================================================================================================

class Stakeholderlog(FlaskForm):
    date = StringField('Date, example 17/02/2019', id='datepick', validators=[DataRequired()])
    stakeholder_person = StringField('Stakeholder name', validators=[DataRequired()])
    organisation = SelectField('Organisation',
    choices=[('BEIS', 'BEIS'), ('Cabinet Office', 'Cabinet Office'), ('CaCHE', 'CaCHE'), ('DCMS', 'DCMS'), ('DfE', 'DfE'), ('DfT', 'DfT'),
    ('DHSC', 'DHSC'), ('DWP', 'DWP'), ('HMRC', 'HMRC'), ('Home Office', 'Home Office'), ('MHCLG', 'MHCLG'), ('MOD', 'MOD'), ('MoJ', 'MoJ'),
    ('NWIS', 'NWIS'), ('ONS', 'ONS'), ('OSR', 'OSR'), ('Welsh Gov', 'Welsh Gov'), ('Other Government Department', 'Other Government Department'),
    ('Other University', 'Other University'), ('Other Private Institution', 'Other Private Institution')], validators=[DataRequired()])
    stance = SelectField('Engagement with best practice',
    choices=[('1', 'Resistant'), ('2', 'Cautious'), ('3', 'Neutral'), ('4', 'Engaged'), ('5', 'Champion')])
    meeting = SelectField('Meeting format',
    choices=[ ('Conference', 'Conference'), ('Informal', 'Informal'), ('One to one', 'One to one'), ('Roundtable', 'Roundtable'), ('Seminar', 'Seminar'), ('Workshop', 'Workshop'),])
    keypoints = StringField('Key points from meeting', validators=[DataRequired()])
    bpier = SelectMultipleField('BPI attendee(s)',
    choices= [])
    #[("Catrin Cheung", "Catrin Cheung"), ("Ramesh  Deonarine", "Ramesh  Deonarine"), ("Anthony G  Edwards", "Anthony G  Edwards"),
     #("Joshua  Halls", "Joshua  Halls"), ("Rebecca  Jones", "Rebecca  Jones"), ("Charles  Lound", "Charles  Lound"), ("David  Mais", "David  Mais"),
     #("Louise  Palmer", "Louise  Palmer"), ("Gentiana  Roarson", "Gentiana  Roarson"), ("Jack  Sim", "Jack  Sim"), ("Connie  Taylor", "Connie  Taylor"),
     #("James  Tucker", "James  Tucker"), ("Nicki  Verdeli", "Nicki  Verdeli"), ("Charlie  Wroth-Smith", "Charlie  Wroth-Smith"),
     #("Holly  Bathgate", "Holly  Bathgate"), ("Liddy  Brankley", "Liddy  Brankley"), ("Catherine A  Davies", "Catherine A  Davies"),
     #("Daisie  Hutchinson", "Daisie  Hutchinson"), ("Sean  Mattson", "Sean  Mattson"), ("Sofi  Nickson", "Sofi  Nickson"), ("William  Perks", "William  Perks"),
     #("Claire  Pini", "Claire  Pini"), ("Caroline  Smith", "Caroline  Smith"), ("Eliza  Swinn", "Eliza  Swinn"), ("Michelle  Bowen", "Michelle  Bowen"),
     #("Holly  Butcher", "Holly  Butcher"), ("Jessica  Evans", "Jessica  Evans"), ("Tegwen  Green", "Tegwen  Green"), ("Martin  Ralphs", "Martin  Ralphs"),
     #("Hannah  Thomas", "Hannah  Thomas"), ("Ami  Treharne", "Ami  Treharne")])
    submit = SubmitField('Submit Data')

#===============================================================================================================

class FilterTable(FlaskForm):
    department = SelectMultipleField('Organisation',
    choices=[('BEIS', 'BEIS'), ('Cabinet Office', 'Cabinet Office'), ('CaCHE', 'CaCHE'), ('DCMS', 'DCMS'), ('DfE', 'DfE'), ('DfT', 'DfT'),
    ('DHSC', 'DHSC'), ('DWP', 'DWP'), ('HMRC', 'HMRC'), ('Home Office', 'Home Office'), ('MHCLG', 'MHCLG'), ('MOD', 'MOD'), ('MoJ', 'MoJ'),
    ('NWIS', 'NWIS'), ('ONS', 'ONS'), ('OSR', 'OSR'), ('Welsh Gov', 'Welsh Gov'), ('Other Government Department', 'Other Government Department'),
    ('Other University', 'Other University'), ('Other Private Institution', 'Other Private Institution')])
    stance = SelectField('Engagement with best practice',
    choices=[("0", "Select Option"),('1', 'Resistant'), ('2', 'Cautious'), ('3', 'Neutral'), ('4', 'Engaged'), ('5', 'Champion')])
    submit = SubmitField("Submit Filter")

#===============================================================================================================

class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

#===============================================================================================================

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')

#===============================================================================================================

class RequestUserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password')

#===============================================================================================================

class SetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Set Password')

#===============================================================================================================

class ChooseGraph(FlaskForm):
    graph_type = SelectField('Variable to plot',
    choices=[("dept", "Organisation"), ("stance", "Stance on Best Practice"), ("meet_type", "Type of Meeting")])
    submit = SubmitField("Submit Filter")

#===============================================================================================================

class DeleteUserForm(FlaskForm):
    user_to_delete = SelectField("Select User to Delete",choices = [])
    submit = SubmitField("Submit Delete")

#===============================================================================================================
