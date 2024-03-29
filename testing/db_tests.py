from database.db import Database
from core.utils import dict_factory


def test_init_db(db: Database = None) -> tuple:
    """
    Tests that the database is initialized correctly.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/store_records.db") if db is None else db

    if db.database_path != "database/store_records.db":
        error = f"Error in test_init_db: Database path is not correct.\n  - Actual: {db.database_path}"
        return False, error
    else:
        return True, "Database path is correct."


def test_get_inventory_exists(db: Database = None) -> tuple:
    """
    Tests that the inventory is not empty.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """

    db = Database("database/store_records.db") if db is None else db
    full_inventory = db.get_full_inventory()

    if len(full_inventory) == 0:
        error = f"Error in test_get_full_inventory: Full inventory is empty.\n  - Actual: {len(full_inventory)}"
        return False, error
    else:
        return True, "Full inventory is not empty."


def test_dict_factory_link(db: Database = None) -> tuple:
    """
    Tests that the row factory is linked to dict_factory.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """
    db = Database("database/store_records.db") if db is None else db
    row_factory = db.connection.row_factory

    if row_factory != dict_factory:
        error = f"Error in test_dict_factory_link: Row factory is not linked to dict_factory.\n  - Expected: {dict_factory}\n  - Actual: {row_factory}"
        return False, error
    else:
        return True, "Row factory is linked to dict_factory."


def test_check_connection_threaded(db: Database = None) -> tuple:
    """
    Tests that the database connection is not single threaded.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string,
    """

    db = Database("database/store_records.db") if db is None else db
    connection_is_threaded = db.connection.isolation_level is None

    if connection_is_threaded:
        error = f"Error in test_check_connection_single_thread: Connection is single threaded.\n  - Actual: {connection_is_threaded}"
        return False, error
    else:
        return True, "Connection is not single threaded."
    
def test_check_product_rating_review(db: Database = None) -> tuple:
    """
    Tests that the product ratings are accurate and valid.

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """
    db = Database("database/store_records.db") if db is None else db
    db.insert_new_sale(9999999999999999,"test",998,100,"999-10-10", 100.0)
    sales = db.get_sales_by_transaction_id(9999999999999999)
    sale_id = sales[0]['sale_id']
    db.set_sale_review(sale_id,'test review')
    db.set_sale_rating(sale_id, 5)
    sale_rating = db.get_sale_rating_by_sale_id(sale_id)
    sale_review = db.get_sale_review_by_sale_id(sale_id)
    if sale_rating != {'sale_rating': 5} or sale_review != {'sale_review': 'test review'}:
        error = f"Error in test_check_product_rating_review: Expected rating and review to be {5} and 'test review' respectively.\n  - Actual rating: {sale_rating}\n  - Actual review: {sale_review}"
        return False, error
    else:
        return True, "review and rating set correctly"
    
def test_is_admin_by_username(db: Database = None) -> tuple:
    """
    Tests that if a user is an admin will return true

    args:
        - db: an sqlite3 database object (optional)

    returns:
        - error_report: a tuple containing a boolean and a string, 
          where the boolean is True if the test passed and False if it failed, 
          and the string is the error report.
    """
    db = Database("database/store_records.db") if db is None else db
    db.insert_user("test1", "dafasf", "test@test.com", "test", "test", 1)

    expected_result = True

    actual_result = db.is_admin_by_username("test1")

    if expected_result != actual_result:
        error = f"Error in test_is_admin_by_username, Expected: {expected_result}, Actual: {actual_result}"
        return False, error
    return True, "is_admin returns correctly"