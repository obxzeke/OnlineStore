#!/usr/bin/env python3

from authentication.auth_tools import login_pipeline, update_passwords, hash_password
from database.db import Database
from flask import Flask, redirect, render_template, request
from core.session import Sessions, UserSession

app = Flask(__name__)
HOST, PORT = 'localhost', 8080
global username, products, db, sessions
username = 'default'
db = Database('database/store_records.db')
products = db.get_inventory_with_reviews()
sessions = Sessions()
sessions.add_new_session(username, db)


@app.route('/')
def index_page():
    """
    Renders the index page when the user is at the `/` endpoint, passing along default flask variables.

    args:
        - None

    returns:
        - None
    """
    products = db.get_inventory_with_reviews()
    return render_template('index.html', username=username, products=products, sessions=sessions)


@app.route('/login')
def login_page():
    """
    Renders the login page when the user is at the `/login` endpoint.

    args:
        - None

    returns:
        - None
    """
    return render_template('login.html')


@app.route('/home', methods=['POST', 'GET'])
def login():
    """
    Renders the home page when the user is at the `/home` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds a new session to the sessions object

    """
    products = db.get_inventory_with_reviews()
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if login_pipeline(username, password):
            is_admin = db.is_admin_by_username(username)
            sessions.add_new_session(username, db)
            global current_username
            current_username = username
            return render_template('home.html', products=products, sessions=sessions, is_admin = is_admin)
        else:
            return redirect('/login?login=false')
    else:
        return render_template('home.html', products=products, sessions=sessions, is_admin = db.is_admin_by_username(current_username))





@app.route('/register', methods=['POST', 'GET'])
def register():
    """
    Renders the index page when the user is at the `/register` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - passwords.txt: adds a new username and password combination to the file
        - database/store_records.db: adds a new user to the database
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        salt, key = hash_password(password)
        update_passwords(username, key, salt)
        db.insert_user(username, key, email, first_name, last_name)
        return render_template('login.html')
    return render_template('register.html')


@app.route('/checkout', methods=['POST'])
def checkout():
    """
    Renders the checkout page when the user is at the `/checkout` endpoint with a POST request.

    args:
        - None

    returns:
        - None

    modifies:
        - sessions: adds items to the user's cart
    """
    order = {}
    user_session = sessions.get_session(username)
    
    for item in products:
        print(f"item ID: {item['id']}")
        if request.form[str(item['id'])] > '0':
            count = request.form[str(item['id'])]
            order[item['item_name']] = [int(count),float(item['price'])]
            user_session.add_new_item(
                item['id'], item['item_name'], item['price'], count)
            db.insert_new_sale(0, username, item['id'], int(count), user_session.date, float(item['price']))

    user_session.update_total_cost()
    user_session.submit_cart()

    return render_template('checkout.html', order=order, sessions=sessions, total_cost=user_session.total_cost,)

@app.route('/reviews', methods=['GET'])
def reviews_page():
    """
    Renders the reviews page

    args:
        - None

    returns:
        - None
    """

    review_info = db.get_reviews_information()

    sales = db.get_sales_by_username(username)
    return render_template('reviews.html', username=username, products=products, sessions=sessions, review_info=review_info, sales=sales)

@app.route('/submit_review/<int:sale_id>', methods=['POST'])
def review_submission(sale_id):
    """
    Handles the review submission when the user submits the review form.

    args:
        - item_id (int): The ID of the item for which the review is being submitted.

    returns:
        - str: A response message indicating the success or failure of the review submission.
    """
    rating = int(request.form.get('rating'))
    review_text = request.form.get('review')

    db.set_sale_rating(sale_id, rating)
    db.set_sale_review(sale_id, review_text)

    return render_template('review_success.html')

@app.route('/admin', methods=['GET'])
def admin_home_page():
    """
    Renders the admin page

    args:
        - None

    returns:
        - None
    """
    return render_template('admin.html')

@app.route('/settings', methods=['GET'])
def settings_page():
    """
    Renders the settings page

    args:
        - None

    returns:
        - None
    """
    return render_template('settings.html')

@app.route('/change_password', methods=['POST','GET'])
def change_password_page():
    """
    Renders the change password page

    args:
        - None

    returns:
        - None

    modifies:
        - user's password
    """
    if request.method == 'POST':
        old_password = request.form['old_password']
        new_password = request.form['new_password']
        if sessions.get_session(current_username).reset_user_password(old_password, new_password):
            return redirect('/change_password?success=true')
        else:
            return redirect('/change_password?success=false')

    return render_template('change_password.html', username = current_username)

@app.route('/view_inventory', methods=['GET'])
def view_inventory():
    """
    Renders the inventory page

        args:
        - None

        returns:
        - None

        modifies:
        - inventory: admin can update stock and price
    """

    if request.method == 'POST':
        try:
            product_id = int(request.form['product_id'])
            price = float(request.form['price'])
            quantity = int(request.form['quantity'])
            if db.product_exists(product_id):
                db.set_item_price(product_id, price)
                db.set_item_stock(product_id, quantity)
            else:
                raise ValueError("Invalid product id")
        except (ValueError, KeyError):
            return redirect('/view_inventory?invalid=true')

    inventory = db.get_full_inventory()
    return render_template('view_inventory.html', inventory = inventory)

@app.route('/see_user_data', methods=['GET'])
def see_user_data():
    """
    Renders the user data page

        args:
        - None

        returns:
        - None
    """
    users = db.get_all_user_information()
    return render_template('see_user_data.html', users=users)

if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
