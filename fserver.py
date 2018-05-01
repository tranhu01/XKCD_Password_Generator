from flask import Flask, render_template
from flask.ext.wtf import Form
from wtforms import SelectField, BooleanField, SubmitField
from passGen import makePasswordList, doLetterSubs, specialPasswordList
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

app.secret_key = 'luthercollege'


class PWSelections(Form):
    minLength = SelectField('Minimum Word Length',
                    choices=[('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8')])

    maxLength = SelectField('Maximum Word Length',
                    choices=[('10','10'),('11','11'),('12','12')])

    maxPwLen = SelectField('Password Length',
                    choices=[('18','18'),('19','19'),('20','20'),('21','21'),('22','22'),
                             ('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),
                             ('28','28'),('29','29'),('30','30')])

    alternate = BooleanField('Easy Typing')
    lettersubs = BooleanField('Number Substitutions')
    phase = BooleanField('Phase: Adjective | Noun | Verb | Adverb')
    submit = SubmitField('Generate Password')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = PWSelections()
    if form.validate_on_submit():
        minLength = int(form.minLength.data)
        maxLength = int(form.maxLength.data)
        maxPwLen = int(form.maxPwLen.data)
        alt = form.alternate.data
        phase = form.phase.data
        if phase:
            pwlist=specialPasswordList(minLength,maxLength,maxPwLen,alt)
        else:
            pwlist = makePasswordList(minLength, maxLength, maxPwLen, alt)
        if form.lettersubs.data:
            doLetterSubs(pwlist)
        return render_template('pwlist.html', pwlist=pwlist)
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
