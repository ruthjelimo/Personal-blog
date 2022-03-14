from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Bio.',validators = [DataRequired()])
    submit = SubmitField('Submit')


class BlogForm(FlaskForm):
    title_blog = StringField('Title')
    description = TextAreaField('Write a Description', validators=[DataRequired()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment = TextAreaField('Write a comment', validators=[DataRequired()])
    submit = SubmitField('Comment')


class SubscriberForm(FlaskForm):
    email = StringField('Your Email Address')
    name = StringField('Enter your name',validators = [DataRequired()])
    submit = SubmitField('Subscribe')

