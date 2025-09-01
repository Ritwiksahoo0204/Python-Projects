from flask import Flask, render_template, request, redirect, url_for, flash
from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

app = Flask(__name__)
app.secret_key = 'coffee123'

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

@app.route('/')
def home():
    items = menu.menu
    return render_template('index.html', items=items)

@app.route('/order/<drink_name>', methods=['GET', 'POST'])
def order(drink_name):
    drink = menu.find_drink(drink_name)
    if not drink:
        flash("Drink not found.")
        return redirect(url_for('home'))

    if not coffee_maker.is_resource_sufficient(drink):
        flash("Not enough resources to make that drink.")
        return redirect(url_for('home'))

    if request.method == 'POST':
        one = int(request.form.get('one', 0))
        two = int(request.form.get('two', 0))
        five = int(request.form.get('five', 0))
        ten = int(request.form.get('ten', 0))
        twenty = int(request.form.get('twenty', 0))

        inserted_amount = (
            one * 1 + two * 2 + five * 5 + ten * 10 + twenty * 20
        )

        success, change = money_machine.process_payment(inserted_amount, drink.cost)

        if success:
            coffee_maker.make_coffee(drink)
            flash(f"Here is your {drink.name} ☕. Enjoy! Change: ₹{change}")
        else:
            flash(f"Not enough money (you inserted ₹{inserted_amount}). Transaction cancelled.")

        return redirect(url_for('home'))

    return render_template('order.html', drink=drink)

@app.route('/report')
def report():
    return render_template('report.html',
        water=coffee_maker.resources["water"],
        milk=coffee_maker.resources["milk"],
        coffee=coffee_maker.resources["coffee"],
        money=money_machine.profit
    )

if __name__ == '__main__':
    app.run(debug=True)
