"""Vehicle Information in rental store """

class Vehicle:
    def __init__(self,type_) -> None:
        self.type_=type_
        
class Bike(Vehicle):
    def __init__(self, type_,brand,sub_type) -> None:
        super().__init__(type_)
        self.brand=brand
        self.sub_type=sub_type        
        
class Car(Vehicle):
     def __init__(self, type_,brand,sub_type,seats) -> None:
        super().__init__(type_)
        self.brand=brand
        self.sub_type=sub_type   
        self.seats=seats
        
        
                