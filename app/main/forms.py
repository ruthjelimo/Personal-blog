from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import DataRequired

class BlogForm(FlaskForm):

  details = TextAreaField('Add your blog', validators=[DataRequired()])
  title = TextAreaField('Add blog title', validators=[DataRequired()])
  submit = SubmitField('Submit')
  
class CommentForm(FlaskForm):
  comment = TextAreaField('Your Comment')
  submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself.',validators = [DataRequired()])
    submit = SubmitField('Submit')