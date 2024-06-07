from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import email_validator
from App.models import User
from flask_login import current_user
from flask_wtf.file import FileField,FileAllowed


class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min = 2, max =28)])
    email = StringField('Email', validators = [DataRequired(), Email()])

    password = PasswordField("PassWord", validators = [DataRequired()])

    confirm_password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password")])
    submit = SubmitField("Sigin Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("The username has been taken")
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("The username has been taken")



class LoginForm(FlaskForm):
    email = StringField('Email',validators = [DataRequired(), Email()])
    password = PasswordField("Confirm Password", validators = [DataRequired(), EqualTo("password")])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")


class UpdateAcoountForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min = 2, max =28)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField("update")

  
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("The username has been taken")
        
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("The username has been taken")

class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content= TextAreaField('Content', validators = [DataRequired()])
    submit = SubmitField("Post")


class ResetRequestForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    submit = SubmitField("Submit")


class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')