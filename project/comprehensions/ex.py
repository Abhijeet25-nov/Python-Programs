"""
    items: A list of dictionaries, each representing a product with keys:
        - "name": str
        - "price": int
        - "category": str
    
    Returns:
        - List of names of affordable products (price < 500)
        - Set of unique categories
        - Dictionary of product name to price mapping
        - Generator expression converted to list of prices after applying 10% discount
"""

def filter_inventory(items: list[dict]) -> tuple[list[str], set[str], dict[str, int], list[int]]:
    item = [
        {"name": "Notebook", "price": 250, "category": "Stationery"},
        {"name": "Pen", "price": 100, "category": "Stationery"},
        {"name": "Bag", "price": 1200, "category": "Accessories"},
        {"name": "Bottle", "price": 400, "category": "Utensils"},
    ]
    
    affordable=[item["name"] for item in items if item["price"]<500]
    categories={item["category"] for item in items}
    price_map={item["name"]:item["price"] for item in items}
    discounted_prices= list((int(item["price"]*0.9) for item in items))
    
    return (affordable,categories,price_map,discounted_prices)

    