"""reducing duplication"""

def print_order(name,chai_type):
    print(f"{name} ordered {chai_type} chai")


print_order("aman","masala")
print_order("aryan","Ginger")
print_order("ajinkya","cinnamon")

"""spliting complex tasks"""

def fetch_sales():
    print("Fetching the sales data")
    
def filter_valid_sales():
    print("Filtering valid sales data")

def summarize_data():
    print("Summerizing sales data")

def generate_report():
    fetch_sales()
    filter_valid_sales() 
    summarize_data()
    print("Report is ready")   
            
generate_report()            

"""HIding implementation details"""

def get_input():
    print("Getting user input")

def validate_input():
    print("Validating the user info")

def save_to_db():
    print("Saving to database")
    
def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registration complete")       
         