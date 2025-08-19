#variable=attribute

class Chai:
    temperature="hot"
    strength="Strong"
    

cutting=Chai()
print(cutting.temperature)    

cutting.temperature="Mild"
cutting.cup="small"                 #type:ignore
print("After changing ",cutting.temperature)
print("cup size is",cutting.cup) #type:ignore
print("Direct look into the class ", Chai.temperature)    

del cutting.temperature
del cutting.cup          #type:ignore
print("After changing ",cutting.temperature)
print("After changing ",cutting.cup)  #type:ignore
