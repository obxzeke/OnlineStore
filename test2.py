from database.db import Database

class test():
    db = Database('database/store_records.db')
    
    print(db.product_exists(1))