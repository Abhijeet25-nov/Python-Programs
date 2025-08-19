"""Sign-up page for any system"""
class UseridInvalidException(Exception): pass
class PasswordInvalidException(Exception): pass

def get_details(name,password:int):
    ''' 1. Correct the paasword saving, use STRING instead of INT
        2. Learn SQL
        3. TRY to implement this same logic in another file but using SQL
    '''
    persons={"abhi2504":2504,"kk2006":2006,"saxenaanita1008":1008,"tnath1970":1970,"shivansh480":480,"absaxena2004":2004,"sony8070":8070}   
    try:
        if name in persons:
            if password == persons[name]:
                print(f"Match found {name} : {password}")
            else:
                raise PasswordInvalidException("Password does not match")
        else:
            raise UseridInvalidException("Sorry ! Your User id not found here")    
    except Exception as e :
        print("Error: ",e)
    finally:
        print("If you get it , ok else Try again...!")   
s=True        
while s:
    name=input("Enter the User-id: ")
    if not isinstance(name,str):
        raise TypeError("User-id should be in string")
    password=int(input("Enter password: "))
    if not isinstance(password,int):
        raise TypeError("Password should be in integer")
    get_details(name,password)
    a=input(("You want to see check more? t/f :").capitalize())
    if a=="t":   
        s=True
    else:
        s=False  
    print("                                    ")
print("Thanking You!")         
