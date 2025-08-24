from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)
CSV_FILE = 'bills.csv'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        bill_id = request.form['bill_id']
        item = request.form['item_name']
        price = float(request.form['item_price'])
        qty = int(request.form['item_quantity'])
        total = price * qty

        with open(CSV_FILE, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([bill_id, item, qty, price, total])

        return redirect('/')
    return render_template('add.html')


@app.route('/remove', methods=['GET', 'POST'])
def remove_item():
    bill_id = None
    items = []

    if request.method == 'POST':
        bill_id = request.form['bill_id']

        # Case: Remove item
        if 'remove_item' in request.form:
            item_name = request.form['remove_item']
            with open('bills.csv', 'r') as file:
                reader = csv.reader(file)
                rows = [row for row in reader if not (row[0] == bill_id and row[1] == item_name)]

            with open('bills.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)

        # Load updated items after deletion or after bill_id submit
        with open('bills.csv', 'r') as file:
            reader = csv.reader(file)
            items = [row for row in reader if row[0] == bill_id]

    return render_template('remove.html', bill_id=bill_id, items=items)




@app.route('/print', methods=['GET', 'POST'])
def print_bill():
    items = []
    total_amount = 0
    tax_rate = 0.18
    tax_amount = 0
    final_amount = 0
    bill_id = ''
    error = ''

    if request.method == 'POST':
        bill_id = request.form['bill_id']
        found = False

        if os.path.exists(CSV_FILE):
            with open(CSV_FILE, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 5 and row[0] == bill_id:
                        items.append({
                            'item_name': row[1],
                            'qty': row[2],
                            'price': row[3],
                            'total_price': row[4]
                        })
                        total_amount += float(row[4])
                        found = True

            if found:
                tax_amount = total_amount * tax_rate
                final_amount = total_amount + tax_amount
            else:
                error = f"No items found for Bill ID '{bill_id}'."
        else:
            error = "Billing file not found."

    return render_template('print.html',
                           bill_id=bill_id,
                           items=items,
                           total=final_amount,
                           error=error)


if __name__ == '__main__':
    app.run(debug=True)
