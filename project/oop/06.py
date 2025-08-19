class Basechai:
    def __init__(self,type_):
        self.type=type_
        
    def prepare(self):
        print(f"Preparing {self.type} chai...") 
        
        
class MasalaChai(Basechai):
    def add_species(self):
        print("Adding Cardamom,ginger,cloves")
        

class ChaiShop:
    chai_cls=Basechai         #hold the reference
    
    def __init__(self) -> None:
        self.chai=self.chai_cls("Regular")        #chai_cls is an object
        
    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()
        

class FancychaiShop(ChaiShop):
    chai_cls = MasalaChai


shop=ChaiShop()
fancy=FancychaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_species()   #type:ignore
    
    
           
         
           