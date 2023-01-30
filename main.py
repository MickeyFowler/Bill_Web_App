from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from RoommatesBill.files import apartment

app = Flask(__name__)


""" test
"""
fgdfggfd
class HomePage(MethodView):

    def get(self):
        return render_template('index.html')


class BillFormPage(MethodView):

    def get(self):
        billform = BillForm()
        return render_template('bill_form_page.html', billform=billform)


class ResultsPage(MethodView):

    def post(self):
        billform = BillForm(request.form)

        the_bill = apartment.Bill(float(billform.amount.data), billform.period.data)
        roommate1 = apartment.Roommate(billform.name1.data, float(billform.days_in_house1.data))
        roommate2 = apartment.Roommate(billform.name2.data, float(billform.days_in_house2.data))

        return render_template('results.html', name1=roommate1.name, amount1=roommate1.pays(the_bill, roommate2), name2=roommate2.name, amount2=roommate2.pays(the_bill,roommate1))


class BillForm(Form):
    amount = StringField("Bill Amount: ")
    period = StringField("Bill Period: ")
    name1 = StringField("Name: ")
    days_in_house1 = StringField("Days in the house: ")
    name2 = StringField("Name: ")
    days_in_house2 = StringField("Days in the house: ")
    button = SubmitField("Calculate payment")


app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))


app.run()

