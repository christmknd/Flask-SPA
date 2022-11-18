from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired,Email,Length

class ContactForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(),Email(message='Invalid email'), Length(max=50)])
    username = StringField('Username', validators=[InputRequired(),Length(min=4,max=15)])
    message = TextAreaField('Message',validators=[InputRequired()])
    submit = SubmitField('Submit')
