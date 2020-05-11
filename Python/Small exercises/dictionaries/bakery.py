
from random import choice
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE!


bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

if food in bakery_stock:
    print(f"{bakery_stock[food]} {food} left!")
else:
    print("We don't carry those!")

    #can also do the following:
    #quantity = bakery_stock.get(food)
#if quantity:
    #print("{} left".format(quantity))
#else:
    #print("we don't make that")