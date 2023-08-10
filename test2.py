from database.db import Database

import os
print(os.getcwd())


class test():
    db = Database('onlineStoreTemplate/database/store_records.db')
    
    print(db.product_exists(1))