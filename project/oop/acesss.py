class chai:
    def __init__(self,type_,strength) -> None:
        self.type=type_
        self.strength=strength
        
        
# class Gingerchai(chai):
#     def __init__(self,type_,strength,spice_level) -> None:
#         self.type=type_
#         self.strength=strength
#         self.spice_level=spice_level

class Gingerchai(chai):
    def __init__(self, type_, strength,spice_level) -> None:
        chai.__init__(self,type_, strength)       #explicit calling          
        self.spice_level=spice_level
        
class GingerChai(chai):
    def __init__(self, type_, strength,spice_level ) -> None:
        super().__init__(type_, strength)    #common method of calling
        self.spice_level=spice_level         #It gives you a way to call methods from a parent (superclass) inside a child (subclass) without explicitly naming the parent.
           