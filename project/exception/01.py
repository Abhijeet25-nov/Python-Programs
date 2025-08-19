orders=["masala","ginger"]
# print(orders[2]) IndexError

"""Try / except"""

chai_menu={"masala":30,"ginger":40}
try:
    chai_menu["elaichi"]
    chai_menu["masala"]
except:
    print("The key that ypu are trying to access does not exists")    

print("Hello chai code")
