loyalty_points=0
def process_transactions(transactions:list[int]) -> int:
        
    def apply_bonus():
        nonlocal sum
        if sum>1000:
            sum +=50
    
    sum=0 
    for amount in transactions:
        sum += amount
    
    apply_bonus()
    
    global loyalty_points
    loyalty_points += sum//100
    
    return sum    
    