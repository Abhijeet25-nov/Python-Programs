from functools import wraps

def require_admin(func):         #decorator func
    @wraps(func)                
    def wrapper(user_role):        #this will replace the original func
        if user_role != "admin":
            print("Access denied: Admins only")
        else:
            return func(user_role)      #run original func
        
    return wrapper      #return modified function

@require_admin
def access_tea_inventory(role):
    print("access granted to tea inventory")
    
    
access_tea_inventory("user")
access_tea_inventory("admin")      
        