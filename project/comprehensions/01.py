"""list comprehension"""
#[expression for item in iterable if condition]

menu =[
    "Masala chai",
    "Iced Lemon Tea",
    "green tea",
    "Iced Peach tea",
    "Ginger chai"
]

iced_tea=[my_tea for my_tea in menu if len(my_tea) <12]
print(iced_tea)
