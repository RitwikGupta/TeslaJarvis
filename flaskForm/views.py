from flask import render_template
from __init__ import app
from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required, Length

lat = 0
lon = 0

class NewForm(Form):
    latitude = TextField('latitude', validators = [Required(), Length(min = 0, max = 20)])
    longitude = TextField('longitude', validators = [Required(), Length(min = 0, max = 20)])
    phone = TextField('phone', validators = [Required(), Length(min = 9, max = 10)])

@app.route('/enter', methods = ['GET', 'POST'])
def enter():
    form = NewForm()
    if form.validate_on_submit():
        lat = form.latitude.data
        lon = form.longitude.data
        phone = form.phone.data
        fo = open("info.txt", 'w')
        fo.write("hi")
        fo.write(lon)
        fo.write(phone)
        fo.close()
        flash('Your changes have been saved.')
        return redirect(url_for('/enter'))
    return render_template('form.html',
        form = form)