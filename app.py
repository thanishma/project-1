import secrets
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# In-memory database
menu_items = []

@app.route('/')
def index():
    return render_template('index.html', menu_items=menu_items)

@app.route('/add', methods=['GET', 'POST'])
def add_menu_item():
    if request.method == 'POST':
        name = request.form.get('name')
        category = request.form.get('category')
        price = request.form.get('price')

        if name and price:
            price = float(price)  # Convert price to float

            menu_item = {'name': name, 'category': category, 'price': price}
            menu_items.append(menu_item)

            flash('Dish added successfully!', 'success')  # Flash success message

            return redirect(url_for('add_menu_item'))
        else:
            flash('Please provide a name and price for the dish.', 'error')  # Flash error message

    return render_template('add_dish.html')


@app.route('/dishes')
def display_dishes():
    total_bill = calculate_total_bill()
    return render_template('dishes.html', menu_items=menu_items, total_bill=total_bill)

@app.route('/delete/<int:index>')
def delete_menu_item(index):
    if 0 <= index < len(menu_items):
        del menu_items[index]

    return redirect(url_for('index'))

def calculate_total_bill():
    total = 0
    for menu_item in menu_items:
        total += menu_item['price']
    return total

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
