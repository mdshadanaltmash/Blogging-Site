from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from companyBlog.models import User

class LoginForm(FlaskForm):

    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField('Password: ',validators=[DataRequired()])
    submit=SubmitField('Log In!')


class RegistrationForm(FlaskForm):

    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField('Username: ',validators=[DataRequired()])
    password=PasswordField('Password: ',validators=[DataRequired(),EqualTo('pass_confirm')])
    pass_confirm=PasswordField('Confirm Password: ',validators=[DataRequired()])
    submit=SubmitField('Register Me!')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your Email has been registered already!')

    def check_email(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')

class UpdateUserForm(FlaskForm):
    email=StringField('Email: ',validators=[DataRequired(),Email()])
    username=StringField('Username: ',validators=[DataRequired()])
    picture=FileField('Update Profile Image: ',validators=[FileAllowed(['jpg','png','jpeg'])])
    submit=SubmitField('Update Me!')

    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your Email has been registered already!')

    def check_email(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Your username has been registered already!')
