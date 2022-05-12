from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *



class location_form(FlaskForm):
    title = StringField("Name", [
        validators.DataRequired()
    ], description="Name of Crypto")

    longitude = StringField("Price", [
        validators.DataRequired()
    ], description="Price Value")

    submit = SubmitField()

