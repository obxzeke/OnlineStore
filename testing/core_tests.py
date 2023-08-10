from core.session import Sessions, UserSession
from database.db import Database
from authentication.auth_tools import hash_password, update_passwords, login_pipeline


def test_init_sessions() -> tuple:
    """
    Tests that the Sessions class is initialized correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    sessions = Sessions()

    if len(sessions.sessions) != 0:
        error = f"Error in test_init_sessions: Sessions dictionary is not empty.\n  - Actual: {len(sessions.sessions)}"
        return False, error
    else:
        return True, "Sessions dictionary is empty."


def test_add_new_session() -> tuple:
    """
    Tests that a new session is added correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/store_records.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)

    if len(sessions.sessions) == 0:
        error = f"Error in test_add_new_session: Sessions dictionary is empty.\n  - Actual: {len(sessions.sessions)}"
        return False, error
    else:
        return True, "Sessions dictionary is not empty."


def test_get_session() -> tuple:
    """
    Tests that a session is retrieved correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/store_records.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)
    session = sessions.get_session("test")

    if not isinstance(session, UserSession):
        error = f"Error in test_get_session: Session is not a UserSession object.\n  - Actual: {type(session)}"
        return False, error
    else:
        return True, "Session is a UserSession object."


def test_get_session_username() -> tuple:
    """
    Tests that a session's username is retrieved correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/store_records.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)
    session = sessions.get_session("test")

    if session.username != "test":
        error = f"Error in test_get_session_username: Session's username is incorrect.\n  - Expected: test\n  - Actual: {session.username}"
        return False, error
    else:
        return True, "Session's username is correct."


def test_get_session_db() -> tuple:
    """
    Tests that a session's database is retrieved correctly.

    args:
        - None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/store_records.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)
    session = sessions.get_session("test")

    if session.db != db:
        error = f"Error in test_get_session_db: Session's database is incorrect.\n  - Expected: {db}\n  - Actual: {session.db}"
        return False, error
    else:
        return True, "Session's database is correct."
    
def test_session_starting_cart() -> tuple:
    """
    Tests that a new session starts with an empty shopping cart.

    args:
        None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string provides a description or error report.
    """
    db = Database("database/store_records.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)
    session = sessions.get_session("test")
    inventory = db.get_full_inventory()
    test_cart = {}
    for item in inventory:
        test_cart[item["id"]] = {"name": item["item_name"], "price": item["price"], "quantity": 0,
                                "discount": 0, "tax_rate": 0}
    if session.get_cart() != test_cart:
        error = f"Error in test_session_starting_cart: Session's starting cart is incorrect.\n  - Expected: {session.get_cart()}\n  - Actual: {test_cart}"
        return False, error
    else:
        return True, "Session's starting cart is correct."
    
    
def test_session_cart_add_item() -> tuple:
    """
    Tests if an item can be successfully added to a session's shopping cart.

    args:
        None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string provides a description or error report.
    """
    db = Database("database/store_records.db")  # Create a database connection (consider using a mock or test DB)
    sessions = Sessions()
    sessions.add_new_session("test", db)
    session = sessions.get_session("test")

    test_item_id = 123
    test_item_name = "Test Item"
    test_item_price = 10.99
    test_quantity = 1
    test_discount = 0.1
    test_tax_rate = 0.05  # Using default tax rate
    
    # Add the item to the session cart
    session.add_new_item(test_item_id, test_item_name, test_item_price, test_quantity, test_discount, test_tax_rate)

    # Check if the item was added to the cart
    if not session.is_item_in_cart(test_item_id):
        error = f"Error in test_session_cart_add_item: Item with ID {test_item_id} was not added to the cart."
        return False, error
    
    return True, "Item was added to the session's cart successfully."

def test_session_cart_price() -> tuple:
    """
    Tests if a cart can succesfully tally price and empty after checkout.

    args:
        None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string provides a description or error report.
    """
    db = Database("database/store_records.db")  # Create a database connection (consider using a mock or test DB)
    sessions = Sessions()
    sessions.add_new_session("test", db)
    session = sessions.get_session("test")

    test_item_id = 123
    test_item_name = "Test Item"
    test_item_price = 10.0
    test_quantity = 1
    test_discount = 0
    test_tax_rate = 0
    
    # Add the item to the session cart
    session.add_new_item(test_item_id, test_item_name, test_item_price, test_quantity, test_discount, test_tax_rate)

    session.submit_cart()

    if session.total_cost != 10.0:
        error = f"Error: Expected session total cost to be 10.0, but got {session.total_cost}."
        return False, error
    
    return True, "total cost was calculated succesfully."

def test_reset_user_password():
    """
    Tests if resetting a password works

    args:
        None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string provides a description or error report.
    """
    db = Database("database/store_records.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)
    sessions = sessions.get_session("test")

    old_password = "test"
    new_password = "updatedPassword"

    new_user_session = UserSession("test", db)
    if new_user_session.reset_user_password(old_password, new_password):
        error = "password didn't reset"
        return False, error

    new_password_hashed = hash_password(new_password)

    updated_password = db.get_password_hash_by_username("test")
    updated_password = updated_password["password_hash"]
    if login_pipeline("test", new_password):
        error = f"Error: Expected new password to be {new_password_hashed[1]} but was {updated_password}"
        return False, error
    return True, "Password was correctly changed"


def test_set_user_password():
    """
    Tests if changing a password works

    args:
        None

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string provides a description or error report.
    """
    db = Database("database/store_records.db")
    sessions = Sessions()
    sessions.add_new_session("test", db)
    sessions = sessions.get_session("test")

    new_password = "password"

    new_user_session = UserSession("test", db)

    new_user_session.set_user_password(new_password)

    actual_password_hashed = db.get_password_hash_by_username("test")
    actual_password_hashed = actual_password_hashed["password_hash"]

    with open("authentication/passwords.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        if line.split(":")[0] == "test":
            salt = line.split(":")[1]
    new_password_hashed = hash_password(new_password, salt)

    if  actual_password_hashed != new_password_hashed[1]:
        error = f"password did not change, Expected {new_password_hashed[1]}, actual {actual_password_hashed}"
        return False, error
    return True, "Password was changed"



