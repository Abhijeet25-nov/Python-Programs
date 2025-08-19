"""Generators"""

#(expression for item in iterable if codnition)
#(x for x in item)-> like a stream

daily_sales=[5,10,12,7,3,8,9,15]

total_cups=sum(sale for sale in daily_sales if sale>5)
print(total_cups)


