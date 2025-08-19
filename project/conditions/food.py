def get_item_price(item: str) -> str:
    
    item_l=item.lower()
    
    match item_l:
        case "pizza":
            return "Price: 30 bucks"
        case "burger":
            return "Price: 15 bucks"
        case "pasta":
            return "Price: 20 bucks"
        case "salad":
            return "Price: 10 bucks"  
        case _:
            return "Item not available"
            