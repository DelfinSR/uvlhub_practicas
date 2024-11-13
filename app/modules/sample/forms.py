from flask_wtf import FlaskForm
from wtforms import SubmitField


class SampleForm(FlaskForm):
    submit = SubmitField('Save sample')
