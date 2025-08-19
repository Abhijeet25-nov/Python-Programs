chai="ginger chai"

def prepare_chai(order):
    print("Preparing ", order)
    
    
prepare_chai(chai)

chai = [1,2,3]
def edit_chai(cup):
    cup[1]=42

edit_chai(chai)
print(chai)    
       
       
#args and kwargs

def special_chai(*ingredients,**extras):
    print("Ingredients",ingredients)
    print("Extras",extras)     
    
   
special_chai("Cinnamon","Cardmom",sweetner="Honey",foam="yes")    

def chai_order(order=None):
    if order is None:
        order=[]
    print(order)
    
chai_order()   