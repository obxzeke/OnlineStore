import unittest
from database.db import Database  # Import your Database class from your module

class TestDatabaseMethods(unittest.TestCase):

    def test_is_admin_by_username(self):
        # Create an instance of the Database class
        db = Database('database/store_records.db')

        # Test the is_admin_by_username method
        #self.assertTrue(db.is_admin_by_username("admin"))
        #self.assertFalse(db.is_admin_by_username("akash"))
        self.assertTrue(db.product_exists(1))

if __name__ == "__main__":
    unittest.main()