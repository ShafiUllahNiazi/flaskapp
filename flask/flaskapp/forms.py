from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    user = StringField('User name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update your profile picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update_profile')


class PostForm(FlaskForm):
    content = TextAreaField("What's on your mind?", validators=[DataRequired()])
    post_image = FileField('post image', validators=[FileAllowed(['jpg', 'png'])])
    post_type = SelectField('Who can see this post',
                            choices=[('public', 'Public'), ('protected', 'Followers'), ('private', 'Only me')])
    submit = SubmitField('Post')
