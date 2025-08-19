class InvalidChaiException(Exception): pass

def bill(flavor,cups):
    menu={"masala":20,"ginger":30}
    try:
        if flavor not in menu:
            raise InvalidChaiException("That chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups should an integer")
        total = menu[flavor] * cups
        print(f"Your bill of {cups} cups of {flavor} flavor chai is:{total}rs ")
    except Exception as e:
       print("Error:",e)
    finally:
        print("Thank you for visiting , Visit again!...")
     
bill("mint",3)
print("-------------------")
bill("masala","three")
print("-------------------")
bill("ginger",4)
            
            