"""Set comprehension"""

#{expression for item in iterable if condition}

fav_chais=[
    "Masala chai",
    "Iced Lemon Tea",
    "green tea",
    "Iced Peach tea",
    "Ginger chai"
]

unique_tea={chai for chai in fav_chais }
print(unique_tea)

receipes={
    "Masala chai":["ginger","cardmom","clove"],
    "Elaichi Chai":["cardmom","milk"],
    "Spicy Chai":["ginger","black pepper","cloves"],
}

unique_speices={spice for ingredients in receipes.values() for spice in ingredients}
print(unique_speices)