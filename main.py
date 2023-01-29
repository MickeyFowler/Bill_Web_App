from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from flask import Flask, render_template, request
from RoommatesBill.files import apartment

app = Flask(__name__)


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
        amount = billform.amount.data
        period = billform.period.data
        name1 = billform.name1.data
        days_in_house1 = billform.days_in_house1.data
        name2 = billform.name2.data
        days_in_house2 = billform.days_in_house2.data

        the_bill = apartment.Bill(float(amount, period))

        roommate1 = apartment.Roommate(float(name1, days_in_house1))
        roommate2 = apartment.Roommate(float(name2, days_in_house2))

        return render_template('results.html', name1=roommate1.name, amount1=roommate1.pays(the_bill, roommate2),
                               name2=roommate2.name, amount2=roommate2.pays(the_bill, roommate1))


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

