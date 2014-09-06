from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length

class NewForm(Form):
    latitude = TextField('latitude', validators = [Required(), Length(min = 0, max = 20)])
    longitude = TextField('longitude', validators = [Required(), Length(min = 0, max = 20)])
    phone = TextField('phone', validators = [Required(), Length(min = 9, max = 10)])

class EditForm(Form):
    nickname = TextField('nickname', validators = [Required()])
    about_me = TextAreaField('about_me', validators = [Length(min = 0, max = 140)])

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)