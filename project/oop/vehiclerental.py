class Engine:
    def __init__(self,_horsepower):
        self._horsepower=_horsepower
    
    def get_engine_info(self):
        return f"{self._horsepower} HP Engine"

class Vehicle:
    _total_vehicle=0
    
    def __init__(self,_brand,_model,_engine:Engine):
        self._brand=_brand
        self._model=_model
        self._engine=_engine
        self._rental_price=0
        Vehicle._total_vehicle+=1 
        
    @staticmethod
    def get_vehicle_type():
        return "Generic Vehicle"
        
    @classmethod
    def get_total_vehicles(cls):
        return cls._total_vehicle
    
    @property
    def rental_price(self):
        
        return self._rental_price
        
    @rental_price.setter
    def rental_price(self,price):
        if price >= 0:
            self._rental_price=price
    
    def get_details(self):
        return f"{self._brand} {self._model} - {self._engine.get_engine_info}"
        
class Car(Vehicle):
    def __init__(self, brand: str, model: str, engine: Engine, seats: int):
        super().__init__(brand, model, engine)
        self.seats = seats
 
    def get_details(self):
        return f"{super().get_details()} - Seats: {self.seats}"       
    
    