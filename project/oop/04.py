class Chaicup:
    size= 150 #ml
    
    def describe(self):  #self is reference or paramater that defines all the properties in the class
        return f"A {self.size}ml chai cup"
    
cup=Chaicup()
print(cup.describe())    
# print(Chaicup.describe())

cup_two=Chaicup()
cup_two.size=100  #type:ignore
print(Chaicup.describe(cup_two))   #type:ignore
