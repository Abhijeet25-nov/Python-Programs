"""Password Strength checker"""

import string
import random
import getpass  #It does not allow to see what the user is passing

def check_password_strength(password):
    issues=[]
    if len(password) < 8:
        issues.append("Too short(min 8 characters should be there)")
    
    #any(c.islower() for c in password) gives a boolean output 
    if not any(c.islower() for c in password) :
        issues.append("-Missing lower case letter")
    if not any(c.isupper() for c in password) :
        issues.append("-Missing upper case letter")      
    if not any(c.isdigit() for c in password) :
        issues.append("-Missing digits")          
    if not any(c in string.punctuation for c in password) :
        issues.append("-Missing a special character")
    return issues 

def generate_strong_password(length=12):
    chars= string.ascii_letters + string.digits + string.punctuation
    
    return "".join(random.choice(chars) for _ in range(length))  

password=getpass.getpass("Enter a password :")
issues= check_password_strength(password)

if not issues:
    print("--strong password! you are good to go--")
else:
    print("---You got weak password")
    for issue in issues:
        print(f"{issue}")
choice=input("DO YOU NEED SUGGESTION? (Y/N): ").upper()
if choice=="Y":        
    print("****Suggesting strong passswords (3)")
    for i in range(3):
        suggestion=generate_strong_password()
        print(suggestion)
print()
print("**********End***********")            