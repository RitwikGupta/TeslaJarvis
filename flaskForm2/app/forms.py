from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required, Length

class NewForm(Form):
    latitude = TextField('latitude', validators = [Required(), Length(min = 0, max = 20)])
    longitude = TextField('longitude', validators = [Required(), Length(min = 0, max = 20)])
    phone = TextField('phone', validators = [Required(), Length(min = 9, max = 10)])