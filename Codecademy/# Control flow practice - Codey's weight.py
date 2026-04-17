# Control flow practice - Codey's weight modifier
print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:
def weight_calc(planet_num: int, current_weight: float) -> None:
    """
    Calculates and prints the weight on a different planet based on a multiplier
    using only if/elif/else statements.

    Args:
        planet_num: An integer (1-6) representing the target planet.
        current_weight: The base weight on Earth.
    """
    # The new weight will be stored here after calculation
    new_weight = 0.0

    # Using if/elif/else to check the planet number and apply the correct multiplier
    if planet_num == 1:
        # Venus: Multiplier 0.91
        new_weight = current_weight * 0.91
        print(f"Codey's weight on planet 1 (Venus) is {new_weight:.2f}")
    elif planet_num == 2:
        # Mars: Multiplier 0.38
        new_weight = current_weight * 0.38
        print(f"Codey's weight on planet 2 (Mars) is {new_weight:.2f}")
    elif planet_num == 3:
        # Jupiter: Multiplier 2.34
        new_weight = current_weight * 2.34
        print(f"Codey's weight on planet 3 (Jupiter) is {new_weight:.2f}")
    elif planet_num == 4:
        # Saturn: Multiplier 1.06
        new_weight = current_weight * 1.06
        print(f"Codey's weight on planet 4 (Saturn) is {new_weight:.2f}")
    elif planet_num == 5:
        # Uranus: Multiplier 0.92
        new_weight = current_weight * 0.92
        print(f"Codey's weight on planet 5 (Uranus) is {new_weight:.2f}")
    elif planet_num == 6:
        # Neptune: Multiplier 1.19
        new_weight = current_weight * 1.19
        print(f"Codey's weight on planet 6 (Neptune) is {new_weight:.2f}")
    else:
        # Handle invalid input
        print("Please provide a valid planet number (1-6).")

weight_calc (1, weight)

#match case statements
user_name = "Dave"  
match user_name:  
    case "Dave":  
        print("Get off my computer Dave!")  
    case "angela_catlady_87":  
        print("I know it is you, Dave! Go away!")   
    case "Codecademy":  
        print("Access Granted.")  
    case default:  
        print("Username not recognized.")  

#magic 8 ball project for if else logic and match case
import random

name = ""
question = "Will my dreams come true"
answer = ""
random_number = random.randint(1,9)
print(random_number)

"""
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
"""

match random_number:
  case 1:
    answer = "Yes - definitely"
  case 2:
    answer = "It is decidedly so"
  case 3:
    answer = "Without a doubt"
  case 4:
    answer = "Reply hazy, try again"
  case 5:
    answer = "Ask again later"
  case 6:
    answer = "Better not tell you now"
  case 7:
    answer = "My sources say no"
  case 8:
    answer = "Outlook not so good"
  case 9:
    answer = "Very doubtful"


if not name:
  print("Question: " + question)
  print("Magic 8-Ball's answer: " + answer)
else: 
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)

#Sal's Shipping
weight = 41.5
ground_price = 0
prem_ground_price = 125
drone_price = 0
# Ground shipping
if weight <= 2: 
  ground_price = weight * 1.5 + 20
  print("For Ground shipping the price is $" + str(ground_price))
elif weight <= 6: 
  ground_price = weight * 3 + 20
  print("For Ground shipping the price is $" + str(ground_price))
elif weight <= 10: 
  ground_price = weight * 4 + 20
  print("For Ground shipping the price is $" + str(ground_price))
elif weight > 10:
  ground_price = weight * 4.75 + 20
  print("For Ground shipping the price is $" + str(ground_price))

# Ground shipping premium
print("For premium ground shipping the price is $" + str(prem_ground_price))

# Drone shipping
if weight <= 2: 
  drone_price = weight * 4.5
  print("For drone shipping the price is $" + str(drone_price))
elif weight <= 6: 
  drone_price = weight * 9
  print("For drone shipping the price is $" + str(drone_price))
elif weight <= 10: 
  drone_price = weight * 12
  print("For drone shipping the price is $" + str(drone_price))
elif weight > 10:
  drone_price = weight * 14.25
  print("For drone shipping the price is $" + str(drone_price))

shipping_options = [
    (ground_price, "Ground Shipping"),
    (prem_ground_price, "Premium Ground Shipping"),
    (drone_price, "Drone Shipping")
]

print(f"--- Shipping Costs for {weight} lbs ---")
print(f"Ground Shipping: ${ground_price:.2f}")
print(f"Premium Ground Shipping: ${prem_ground_price:.2f}")
print(f"Drone Shipping: ${drone_price:.2f}")
print("--------------------------------------")

# 2. Loop to find the cheapest price
cheapest_price = float('inf')  # Start with an infinitely high price
cheapest_method = ""

for price, method in shipping_options:
    if price < cheapest_price:
        # If the current price is lower than the current cheapest, update
        cheapest_price = price
        cheapest_method = method

# 3. Output the result
print(f"The CHEAPEST option for a {weight} lb package is:")
print(f"Method: {cheapest_method}")
print(f"Cost: ${cheapest_price:.2f}")