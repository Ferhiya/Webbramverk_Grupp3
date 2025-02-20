from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SelectField, SubmitField, SelectMultipleField
from wtforms.validators import DataRequired, Email, Length
from models import Role

class ContactForm(FlaskForm):
    name = StringField('Namn', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()], render_kw={"class": "message-box"})
    submit = SubmitField('Skicka')

class UserForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    role = SelectMultipleField('Roles', coerce=int, validators=[DataRequired()])  
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Create User')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name) for role in Role.query.all()]