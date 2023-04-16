# A program to organize sales data
# Author: Sirisha Adivishnu
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
number_of_as = prices.count(2)
print(number_of_as)

num_pizzas = len(toppings) 
print("We sell" + str(num_pizzas), "different kinds of pizza!")
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)
cheapest_pizza = pizza_and_prices.sort()
priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop(-1)
pizza_and_prices.insert(4, [2.5, "peppers"])

print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
