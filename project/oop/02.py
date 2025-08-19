#concept of namespaces: objects has its own identy own behaviour but cannot bothers others

class Chai:
    origin="India"
    
print(Chai.origin)  

Chai.is_hot=True  # type: ignore
print(Chai.is_hot) # type: ignore
  
#creating objects from class Chai
masala=Chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")  # type: ignore
masala.is_hot = False    # type: ignore

print("class :",Chai.is_hot) # type: ignore
print(f"Masala {masala.is_hot}") # type: ignore

masala.flavour="Masala" # type: ignore
