import os
from flask import Flask, request, render_template, jsonify, session, redirect, url_for, make_response
from wtforms import Form, TextAreaField, validators
from wtforms import StringField,SelectField,TextAreaField,SubmitField
from wtforms.validators import DataRequired # Need data before submit.
from flask_wtf import FlaskForm
# SQL Module Imports

import sys


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'




class InfoForm(FlaskForm):
    '''
    This general class gets a lot of form about puppies.
    Mainly a way to go through many of the WTForms Fields.
    '''

    firmname = StringField('Firm name',validators=[DataRequired()])
    abstract = TextAreaField('Patent abstract',validators=[DataRequired()])
    submit = SubmitField('Submit')

class PlotForm(FlaskForm):
    class_list_label = ['A','B']
    selects_class = SelectField('Class',choices=class_list_label)
    submit = SubmitField('Submit')



# Home page
@app.route('/', methods=['GET', 'POST'])
def index():
    form_info = InfoForm()
    # form_plot = PlotForm()
    if request.method == 'POST' and form_info.validate_on_submit():
        try:
            firmname = request.form['firmname']
            abstract = request.form['abstract']
            sql_abstract=f"insert into classify(firmname,abstract) values('{firmname}','{abstract}')"
            cur.execute(sql_abstract)
            conn.commit()
        except:
            return "Database connection error."
    return render_template('01_home.html',form_info=form_info)

@app.route('/subplot',methods=['GET', 'POST'])
def getsubplot():
    form_plot = PlotForm()
    selects_class=form_plot.selects_class.data
    if request.method == 'POST' and form_plot.validate():
        try:
            selects_class = request.form['selects_class']
        except:
            return "Plot error."
    return render_template('02_subplot.html',form_plot=form_plot,selects_class=selects_class)
'''
@app.route('/result')
def getresult(form_info):
    return render_template('03_result.html',form_info=form_info,firmname=form_info.firmname.data,abstract=form_info.abstract.data)

'''
IMG_PATH = "./templates/wordcloud_img/"


@app.route('/display/img/<string:filename>', methods=['GET'])
def display_img(filename):
    if request.method == 'GET':
        if filename is None:
            pass
        else:
            image_data = open(IMG_PATH + filename, "rb").read()
            response = make_response(image_data)
            response.headers['Content-Type'] = 'image/jpg'
            return response
    else:
        pass


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5432))
    app.run(host='0.0.0.0', port=port, debug=True)
