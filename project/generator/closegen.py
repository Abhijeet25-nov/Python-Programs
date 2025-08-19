from traceback import print_list


def local_chai():
    yield "Masala chai"
    yield "Ginger chai"
    
def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()
    
for chai in full_menu():
    print(chai)  
    
def chai_stall():
    try:
        while True:
            order=yield "Waiting for chai order"
    except:
        print("Stall closed,No more chai")
 
stall = chai_stall()
print(next(stall)) 
stall.close()          #cleaning up the memory                  