import authentication.auth_tools as auth
import core.session as c

#tests to see if the login works for valid logins
def auth_login_test() -> bool:
     validUser = auth.login_pipeline("admin", "admin")
     invalidUser = auth.login_pipeline("admin", "444")
     if validUser and not invalidUser:
         return True
     else:
         return False
     
#tests to see if the inventory will add and delete a test product without errors
def core_inventory_test() -> bool:
    try:
        c.AdminSession.update_Product_inventory(95959, 1)
        c.AdminSession.remove_product(95959) 
        return True   
    except:
        return False
         

#runs the 2 tests
if __name__ == "__main__":
    if auth_login_test:
        print("authentication login test passed")
    else:
        print("authentication login test failed")
        
    if core_inventory_test():
        print("core inventory test passed")
    else: 
        print("core inventory test failed")