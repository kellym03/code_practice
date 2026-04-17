# Lists
# Gradebook project
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["physics","calculus","poetry","history"]
grades = [98,97,85,88]

gradebook = [["physics",98],["calculus",97],["poetry",85],["history",88]]

print(gradebook)

gradebook.append(["computer science",100])
print(gradebook)

gradebook.append(["visual arts",93])
print(gradebook)

gradebook[-1][-1] = 98
print(gradebook)

# removes the value from index 2, poetry from the sublist
gradebook[2].remove(85)
print(gradebook)

gradebook[2].append("Pass")
print(gradebook)

full_gradebook = last_semester_gradebook + gradebook
print(f"Your full gradebook is the following {full_gradebook}")

# Working with lists
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
print(inventory_len)

first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count("twin bed")
removed_item = inventory.pop(4) # removes item at index 4
print(inventory)
inventory.insert(10, "19th Century Bed Frame")
inventory.sort()
#Remember, the sorted() function doesn’t change the original list — it creates a new list with the elements properly sorted. If you use sorted() you’ll have to set inventory equal to the value returned by sorted().
print(inventory)

# animals.insert(2, "fox") # inserts "fox" at index 2

"""
friends = ["Annabelle", "Greg", "Katya", "Sol"]
friends.insert(2, "Jess") # inserts "Jess" at index 2
"""

game_results.count("win") # counts number of times "win" appears in list

#Len's slice
# Your code below:
toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices = [2,6,1,3,2,7,2]

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

num_pizzas = len(toppings)
print(f"We sell {num_pizzas} different kinds of pizza!")

zipped_data = zip(prices, toppings)
pizza_and_prices = [list(item) for item in zipped_data]

print(pizza_and_prices)

pizza_and_prices.sort()
print(pizza_and_prices)
cheapest_pizza = pizza_and_prices[0]
print(cheapest_pizza)
priciest_pizza = pizza_and_prices[-1]
print(priciest_pizza)
pizza_and_prices.pop(-1)
print(pizza_and_prices)
pizza_and_prices.append([2.5, "peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)

three_cheapest = pizza_and_prices[:3]
print(three_cheapest)


"""
Tuples are one of the built-in data structures in Python. Just like lists, tuples can hold a sequence of items and have a few key advantages:

Tuples are more memory efficient than lists
Tuples have a slightly higher time efficiency than lists
This is mostly because tuples are immutable, meaning we can’t modify a tuple’s elements after creating one, and do not require an extra memory block like lists. Because of this, tuples are great to work with if you are working with data that won’t need to be changed in your code.

In this article, we’ll cover features of tuples, indexing, and common built-in methods and functions that can be used with tuples.
They are stored in brackets () instead of [] like lists. They can be sliced and indexed the same way as lists, but they cannot be modified after creation.
"""

my_tuple = ('abc', 123, 'def', 456)
