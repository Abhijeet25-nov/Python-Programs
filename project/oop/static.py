class chaiutils:
    @staticmethod                 #does not need self
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    
    
    
raw="water, milk, ginger, honey" 

obj=chaiutils()
cleaned=chaiutils.clean_ingredients(raw)
print(cleaned)
print("--------------------------------------------------") 


#@class method receives cls (class itself), operate on class not on instance
  
  
class chaiorder:
    
    def __init__(self,tea_type ,sweetness,size) :
        self.tea_type =tea_type
        self.sweetness=sweetness
        self.size=size
    
    @classmethod
    def from_dict(cls,order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls,order_string):
        tea_type,sweetness,size=order_string.split("-")
        return cls(tea_type,sweetness,size)    

class chaisize:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small" ,"Medium","Large"]
        
order1=chaiorder.from_dict({"tea_type" : "Masala","sweetness":"medium","size": "Large"}) 
print(order1.__dict__)
order2=chaiorder.from_string("Ginger-Low-Small")
print(order2.__dict__)         

order3=chaiorder("large","low","Large")
print(order3.__dict__)