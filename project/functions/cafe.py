# LOCAL- inside a function
# Enclosing from outer function if nested
# global - Top level script
# built in

def serve_chai():
    chai_type="Masala" #local scope
    print(f"Inside function : {chai_type}")

chai_type="Lemon" #global
serve_chai()
print(f"Outside function : {chai_type}")

def chai_counter():
    chai_order="lemon" #enclosing scope
    def print_order():
        chai_order="Ginger"
        print("Inner:",chai_order)
    print_order()
    print("Outer:",chai_order)    
    
chai_order="Tulsi" #Global
chai_counter()
print("Global :",chai_order)


print("""""""""""""""""")
#for non local varible should be inside inside a outer function
def update_order():
    chai_type="Elaichi"
    
    def kitchen():
        nonlocal chai_type
        chai_type="Kesari"
    kitchen()
    print("after kitchen update",chai_type)
    
print(update_order())