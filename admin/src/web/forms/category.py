from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class CategoryForm(FlaskForm):
    name = StringField("Name")
    description = StringField("Description")
    submit = SubmitField("Submit")
