#getter and setters

class Tealeaf:
    def __init__(self,age):
        self._age=age
        
    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self,age):
        if 1<=age<=5:
            self._age=age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years") 

leaf = Tealeaf(7)
print(leaf.age)

leaf.age=7
print(leaf.age)

        
               