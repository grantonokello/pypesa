from flask import Flask, request, render_template, abort, flash
from wtforms import Form, StringField, IntegerField, TelField, SubmitField
from wtforms.validators import DataRequired
from pypesa import c2b, status

class C2b(Form):
    number = TelField("enter phone number", validators=[DataRequired()])
    amount = IntegerField("enter amount", validators=[DataRequired()])
    item = StringField("enter the name of the item", validators=[DataRequired()])
    submit = SubmitField("submit")

# intialise flask
web = Flask(__name__)

@web.route("/", methods=["post", "GET"])
def main():
    form = C2b()
    if form.validate():
        number = form.number.data
        amount = form.amount.data
        item = form.item.data
        function = c2b(amount, number, item)
    return render_template("form.html", form=form)


@web.route("/confirm")
def confirm():
    state =  status()
    if state == "1":
        flash("Payment successful")
    else:
        flash("Payment unsucceful")
    return



if __name__=="__main__":
    web.run(debug=True)
