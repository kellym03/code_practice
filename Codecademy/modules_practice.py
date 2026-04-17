#Modules practice
#custom_module
def generate_time_travel_message(year, destination, cost):
  print(f"Pack your bags! You're traveling to {destination} in the year {year}. The cost of this trip will be ${cost}.")

#time_travelers_toolkit.py
import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
import custom_module

print(f"Today's date is {dt.date.today()} and the time is {dt.datetime.now().time()}")

base_cost = Decimal(0.01)
target_year = randint(0,3000)
current_year = Decimal(dt.date.today().year)

cost = abs(base_cost * (current_year-target_year))
cost = round(cost, 2)

print(cost)
destinations = ["Tokyo", "Berlin", "London", "Sydney", "Los Angeles"]
destination_choice = choice(destinations)

custom_module.generate_time_travel_message(target_year,destination_choice,cost )