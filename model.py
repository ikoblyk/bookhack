# model.py
from wtforms import SubmitField, BooleanField, StringField, PasswordField, validators, ValidationError
import re
from flask_wtf import Form
class URLForm(Form):
    url = StringField('URL',[validators.DataRequired()])
    def validate_url(form, field):
        reg = re.compile(r"https://elib.nlu.org.ua/view.html\?&id=\d+")
        if reg.fullmatch(field.data) is None:
            raise ValidationError("Wrong URL!!!")
    submit = SubmitField('Download')