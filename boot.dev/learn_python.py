#Variables

#F strings
num_bananas = 10
bananas = f"You have {num_bananas} bananas"
print(bananas)
# You have 10 bananas

#None type
#None is a special value in Python that represents the absence of a value. 
# create the empty "enemy" variable here
enemy = None

# don't touch below this line
print(enemy is None) # True, change the enemy value it becomes false

#Dynamic typing
#Languages that aren't dynamically typed are statically typed, such as Go and Typescript (one of which you'll learn in a later course depending on your chosen track). In a statically typed language, if you try to assign a value to a variable of the wrong type, you'll get a compile-time error and the program won't run.
#Python is dynamic and the type of a variable will change depending on the value assigned

#Multi Variable declaration
sword_name, sword_damage, sword_length = "Excalibur", 10, 200
#Is the same as 
sword_name = "Excalibur"
sword_damage = 10
sword_length = 200

#print() vs return
#print() is a function that:
#Prints a value to the console
#Does not return a value

#return is a keyword that:
#Ends the current function's execution
#Provides a value (or values) back to the caller of the function
#Does not print anything to the console (unless the return value is later print()ed)

# Most Python developers solve this structuring early functions in scripts by defining all the functions in their program first, then they call an "entry point" function at the end of the file. 
# That way all of the functions have been read by the Python interpreter before the first one is called.

# No return in function
#When no return value is specified in a function, it will automatically return None. For example, maybe it's a function that prints some text to the console, but doesn't explicitly return a value. 

# Multiple return values
def cast_iceblast(wizard_level, start_mana):
    damage = wizard_level * 2
    new_mana = start_mana - 10
    return damage, new_mana # return two values

# Receive Multiple values
damage, mana = cast_iceblast(5, 100) #Lined up the variables in the single line because you know the function called will return multiple values
print(f"Damage: {damage}, Remaining Mana: {mana}")
# Damage: 10, Remaining Mana: 90

#Unit Tests
#Going forward, you'll encounter a new type of lesson: unit tests. A unit test is just an automated program that tests a small "unit" of code. Usually just a function or two.
# On boot.dev there are two types of lessons, unit tests and console output tests. 
# Unit tests will not require me to delete my print statements but just match the outputs in the paired main_test.py file.
# Console output tests will require the output of my code to match the expectations of console and there is no paired main_test.py file.

#Solving hard problems on boot.dev
#Process for Solving Hard Coding Problems
#Read the lesson first! Figure out the examples before writing your own code.
#Read the assignment. Understand the goal of the assignment before you start writing code.
#Start writing code.
#Add print() statements. Don't wait until you've written a lot of code to start testing. Add print() statements and use the Run button to see if your code is doing what you expect at each step. It's easier to find issues in small bits of code than in large blocks of code.
#Keep running, printing, and fixing until you're confident your code is working.
#Submit your code. If the assignment you're working on has unit tests, no need to remove your debugging print() statements. If the assignment you're working on is testing console output, be sure to remove your print() statements before submitting.
#Compare your code to the instructor's. You will not be penalized for looking at the solution after you have successfully completed the assignment.

#Stack Trace or Trace Error
#A stack trace (or "traceback") is a scary-looking error message that the Python interpreter prints to the console when it encounters certain problems. Stack traces are most common (at least for you right now) when you're trying to run invalid Python code.
#Example below:
Traceback (most recent call last): #This is a standard header that's just letting us know we're looking at a traceback.
  File "<string>", line 1, in <module> #This is the start of the "trace". This strange "<string>" file doesn't really exist! It's part of how the virtual browser-based environment of the Python interpreter works!
  File "/home/pyodide/main.py", line 3 #In this case, the interpreter was executing the code in the main.py file when it encountered an error on line 3.
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats. #Now we're getting to the real meat of the error message! The purpose of a "trace" is to take us step-by-step along the path that the Python interpreter took through our code before it encountered an error. More often than not, this will help us figure out what went wrong! #This is the actual line of code that caused the error.
                                                                                                                  ^
IndentationError: unindent does not match any outer indentation level #This is the error type. In this case, it's an IndentationError! The Python interpreter expected a certain amount of indentation (whitespace at the beginning of the line) but didn't find what was expected.
PythonError

#Floor division - Rounds down to the nearest INTEGER. This is part of the reason python has been successful in machine learning. 
7 // 3
# 2 (an integer, rounded down from 2.333)
-7 // 3
# -3 (an integer, rounded down from -2.333)

# Incrementing values
# can use +=, *=, -= /=
#You cannot use -= in a return statement. Set the variable first, and then return it after!

#Scientific Notaiton
#In a nutshell, the number following the e specifies how many places to move the decimal to the right for a positive number, or to the left for a negative number.
print(16e3)
# Prints 16000.0

print(7.1e-2)
# Prints 0.071

#Underscore for readability
num = 16_000
print(num)
# Prints 16000

num = 16_000_000
print(num)
# Prints 16000000

#Binary in Python - Binary is just base 2 on or off signals read from right to left
print(0b0001)
# Prints 1

print(0b0101)
# Prints 5

#Bitwise operations
# A 1 in binary is the same as True, while 0 is False. So really a bitwise operation is just a bunch of logical operations that are completed in tandem by column.

0101 #5
&
0111 #7
=
0101 #5
---
0101 #5
&
0010 #2
=
0000 #0

#Therefore 
0b0101 & 0b0111
# equals 5

binary_five = 0b0101
binary_seven = 0b0111
binary_five & binary_seven
# equals 5

#More examples of bitwise operations
can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    user_create_guild_permission = user_permissions & can_create_guild
    return user_create_guild_permission
print(get_create_bits(0b1001))
print(get_create_bits(0b0001))

def get_review_bits(user_permissions):
    user_review_guild_permission = user_permissions & can_review_guild
    return user_review_guild_permission


def get_delete_bits(user_permissions):
    user_delete_guild_permission = user_permissions & can_delete_guild
    return user_delete_guild_permission


def get_edit_bits(user_permissions):
    user_edit_guild_permission = user_permissions & can_edit_guild
    return user_edit_guild_permission

# Bitwise '|' (pipe) operator, the OR operator in bitwise
def calculate_guild_perms(glorfindel, galadriel, elendil, elrond):
    party_perms = glorfindel|galadriel|elendil|elrond
    return party_perms

print(calculate_guild_perms(0b1000, 0b0000, 0b0010, 0b0001)) #11

#Binary string conversions
# this is a binary string
binary_string = "100"

# convert binary string to integer
num = int(binary_string, 2) #The two represents base 2, if this were base 10 it would be 100
print(num)
# 4

#My code for bitwise binary string conversion
def binary_string_to_int(num_servers, num_players, num_admins):
    int_num_servers = int(num_servers, 2)
    int_num_players = int(num_players, 2)
    int_num_admins = int(num_admins, 2)
    return int_num_servers, int_num_players, int_num_admins

a, b, c = binary_string_to_int("100", "110", "101")
print(a)
print(b)
print(c)

#Objective is to return a boolean, I could put the logic expression in the return statement it still returned the Boolean value correctly
def player_1_wins(player_1_score, player_2_score):
    return player_1_score > player_2_score

#Comparison Operators 
def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    is_mustang_edward_same = edward_height == mustang_height
    is_alphonse_edward_same = alphonse_height == edward_height
    is_winry_alphonse_same = winry_height == alphonse_height
    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same


print(compare_heights(100, 101, 102, 100))

#If statement
def print_status(player_health):
    if player_health <= 0:
        print("dead")
        print("status check complete")
        return
    print("status check complete")

#A continue statement immediately halts the current iteration and jumps to the next one, which saves the program from doing unnecessary work.
#For example, if we're calculating square roots, we might want to skip negative numbers. 
# continue lets us move on to the next number without wasting any time:

for number in range(-5, 5):
    if number < 0:
        continue  # Skip negatives

    print(f"The square root of {number} is {number ** 0.5}")

#The square root of 0 is 0.0
#The square root of 1 is 1.0
#The square root of 2 is 1.4142135623730951
#The square root of 3 is 1.7320508075688772
#The square root of 4 is 2.0

def award_enchantments(start, end, step):
    counter = 0
    for quest_number in range(start, end, step):
        counter += 1
        if counter < 3:
            continue # Basically saying skip to the next iteration in the loop, ignore the code below this
        counter = 0
        enchantment_strength = quest_number * 5
        print(
            f"Enchantment of strength {enchantment_strength} awarded for completing {quest_number} quests!"
        )

#Break statements end a loop entirely
#We can use continue to skip to the next iteration in a loop, but what if we want to exit the loop entirely? That's where the break statement comes in.

#Lists
#list[i] - Use square brackets and it will trigger the list indice search
#.append() will add an item to the end of a list 
#.pop() will remove the last item from a list

#No-index syntax
#tree, the variable declared using the in keyword, directly accesses the value in the list rather than the index of the value. 
# If we don't need to update the item and only need to access its value then this is a more clean way to write the code.
trees = ['oak', 'pine', 'maple']
for tree in trees:
    print(tree)
# Prints:
# oak
# pine
# maple


# Slicing Lists
# Python makes it easy to slice and dice lists to work only with the section you care about. 
# One way to do this is to use the simple slicing operator, which is just a colon :.
# With this operator, you can specify where to start and end the slice, and how to step through the original list. 
# List slicing returns a new list from the existing list.
# The syntax is as follows:

my_list[ start : stop : step ]

F#or example:

scores = [50, 70, 30, 20, 90, 10, 50]
# Display list
print(scores[1:5:2])
# Prints [70, 20]

# The above reads as "give me a slice of the scores list from index 1, up to but not including 5, skipping every 2nd value". 
# All of the sections are optional.

# Omitting Sections
# You can also omit various sections ("start", "stop", or "step"). For example, numbers[:3] means "get all items from the start up to (but not including) index 3". numbers[3:] means "get all items from index 3 to the end".

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[:3] # Gives [0, 1, 2]
numbers[3:] # Gives [3, 4, 5, 6, 7, 8, 9]

# Using Only the “step” Section
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[::2] # Gives [0, 2, 4, 6, 8]

# Negative Indices
# Negative indices count from the end of the list. For example, numbers[-1] gives the last item in the list, numbers[-2] gives the second last item, and so on.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[-3:] # Gives [7, 8, 9]

#List Operations - Contains
#Checking whether a value exists in a list or not is also really easy in Python: just use the in keyword to check for presence, or not in to check for absence.
fruits = ["apple", "orange", "banana"]
print("banana" in fruits)
# Prints: True

fruits = ["apple", "orange", "banana"]
print("banana" not in fruits)
# Prints: False

#List Deletion
#Python has a built-in keyword del that deletes items from objects. In the case of a list, you can delete specific indexes or entire slices.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# delete the fourth item
del nums[3]
print(nums)
# Output: [1, 2, 3, 5, 6, 7, 8, 9]

# delete the second item up to (but not including) the fourth item
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[1:3]
print(nums)
# Output: [1, 4, 5, 6, 7, 8, 9]

# delete all elements
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del nums[:]
print(nums)
# Output: []

#Tuples are collections of data that are ordered and unchangeable. You can think of a tuple as a List with a fixed size. Tuples are created with round brackets:
my_tuple = ("this is a tuple", 45, True)
print(my_tuple[0])
# this is a tuple
print(my_tuple[1])
# 45
print(my_tuple[2])
# True
#There is a special case for creating single-item tuples. You must include a comma so Python knows it's a tuple and not regular parentheses:
dog = ("Fido",)

#Reverse List 
def reverse_list(items):
    new_list = []
    for i in range(len(items)-1,-1,-1):
        new_list.append(items[i])
    return new_list

#Split a String Into a List of Words
#The .split() method in Python is called on a string and returns a list by splitting the string based on a given delimiter. If no delimiter is provided, it will split the string on whitespace. Here's a quick example:

message = "hello there sam"
words = message.split()
print(words)
# Prints: ["hello", "there", "sam"]

#Join a List of Strings Into a Single String
#The .join() method is called on a delimiter (what goes between all the words in the list), and takes a list of strings as input.

list_of_words = ["hello", "there", "sam"]
sentence = " ".join(list_of_words)
print(sentence)
# Prints: "hello there sam"

def filter_messages(messages):
    dang_removed = []
    count_of_dangs_list = []
    for message in messages:
        words = message.split()
        #print(words)
        good_words = []
        dang_count = 0
        for word in words:
            if word == "dang" or word == "Dang":
                dang_count +=1
            else:
                good_words.append(word)
        dang_removed.append(" ".join(good_words))
        count_of_dangs_list.append(dang_count)
    return dang_removed, count_of_dangs_list

print(filter_messages(["darn it", "this dang thing won't work", "lets fight one on one"]))

#Even Teams
def get_even_and_odd_teams(players):
    evens = []
    odds = []
    for i in range(0,len(players)):
        if i % 2 == 1:
            odds.append(players[i])
        if i % 2 == 0:
            evens.append(players[i])
    return evens, odds
    
#Dictionaries
#To access a value in a dictionary, dict["key_name"]

#Setting dictionary values
planets = {}
planets["Earth"] = True
planets["Pluto"] = False
print(planets["Pluto"])
# Prints False

#Delete dictionary values
names_dict = {
    "jack": "bronson",
    "jill": "mcarty",
    "joe": "denver"
}

del names_dict["joe"]

print(names_dict)
# Prints: {'jack': 'bronson', 'jill': 'mcarty'}

#Checking practice
#If you're unsure whether a key exists in a dictionary, use the in keyword.
cars = {
    "ford": "f150",
    "toyota": "camry"
}

print("ford" in cars)
# Prints: True

print("gmc" in cars)
# Prints: False

#Counting practice
#Checking for existence
def count_enemies(enemy_names):
    enemies_dict = {}
    for enemy_name in enemy_names:
        if enemy_name in enemies_dict:
            enemies_dict[enemy_name] += 1
        else:
            enemies_dict[enemy_name] = 1
    return enemies_dict

#Iterating over a dictionary in Python
#We can iterate over a dictionary's keys using the same no-index syntax we used to iterate over the values in a list.
#With access to the dictionary's keys, we also have access to their corresponding values.

fruit_sizes = {
    "apple": "small",
    "banana": "large",
    "grape": "tiny"
}

for name in fruit_sizes:
    size = fruit_sizes[name]
    print(f"name: {name}, size: {size}")

# name: apple, size: small
# name: banana, size: large
# name: grape, size: tiny

#Assignment for iterating through a python dictionary - the trick was to have two variable set based on the a condition within a for loop
def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    largest_enemy = ""
    for enemy in enemies_dict:
        if enemies_dict[enemy] > max_so_far:
            max_so_far = enemies_dict[enemy]
            largest_enemy = enemy
    if max_so_far == float("-inf"):
        return None
    else:
        return largest_enemy

#Ordered or Unordered?
#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries were unordered.
#Because dictionaries are ordered, the items have a defined order, and that order will not change.
#Unordered means that the items do not have a defined order.
#The takeaway is that if you're on Python 3.7 or later, you'll be able to iterate over dictionaries in the same order every time.

#Accessing nested dictionaries
def get_quest_status(progress):
    return progress["quests"]["bridge_run"]["status"]

#Merging Dictionaries
def merge(dict1, dict2):
    merged_dict = dict1 #Just created a copy of dict1 as the starting template for merged dict to save time
    for key, value in dict2.items(): #Can create two temp values in for loops for dictionaries - been a while since using this
        merged_dict[key] = value
    return merged_dict

#Boot.dev solution to merging was:
def merge(dict1, dict2):
    merged_dict = {}
    for key in dict1:
        merged_dict[key] = dict1[key] #merged_dict[key] created the key and = dict1[key] assigned the value 
    for key in dict2:
        merged_dict[key] = dict2[key]
    return merged_dict

#Sets
Sets are like Lists, but they are unordered and they guarantee uniqueness. Only ONE of each value can be in a set.
fruits = {"apple", "banana", "grape"}
print(type(fruits))
# Prints: <class 'set'>

print(fruits)
# Prints: {'banana', 'grape', 'apple'}

#Add values to a set
fruits = {"apple", "banana", "grape"}
fruits.add("pear")
print(fruits)
# Prints: {'pear', 'banana', 'grape', 'apple'}

#No error will be raised if you add an item already in the set, and the set will remain unchanged.

#An empty set
#Because the empty bracket {} syntax creates an empty dictionary, to create an empty set, you need to use the set() function.

#Add to a set
fruits = set()
fruits.add("pear")
print(fruits)
# Prints: {'pear'}

#Remove from a set
fruits = {"apple", "banana", "grape"}
fruits.remove("apple")
print(fruits)
# Prints: {'banana', 'grape'}

#Set iteration works like the below however you can see that the printed order isn;t what the order of the set is, as it is unordered
fruits = {"apple", "banana", "grape"}
for fruit in fruits:
    print(fruit)
    # Prints:
    # banana
    # grape
    # apple
#Set Assignment
def remove_duplicates(spells):
    seen_spells = set(spells) #This will automatically deduplicate a set if putting it in a set
    print(seen_spells)
    unique_spells = []
    for spell in seen_spells:
        unique_spells.append(spell)
    return unique_spells

#Set subtraction - this is all quite useful for quick duplication
def find_missing_ids(first_ids, second_ids):
    first_ids_set = set(first_ids)
    second_ids_set = set(second_ids)
    unique_id_set = first_ids_set - second_ids_set
    return unique_id_set

#Exceptions
#Errors detected during execution are called "exceptions" even if they have correct syntax
try:
  10 / 0
except Exception:
  print("can't divide by zero")

#the except block will only execute when there is an Exception
#If we want to access the data from the exception it will be like the below 
try:
  10 / 0
except Exception as e:
  print(e)

# prints "division by zero"
# If an exception is raised outside of the code block it will work its way up the train until it finds a try block. If it cannot find a try block it will crash the program and print and error saying Exception. 

#Seems like what the exception message is needs to be defined with something like, raise Exception("player id not found")
#Dont catch your own exceptions inside the function block
# don't do this
def craft_sword(metal_bar):
    try:
        if metal_bar == "bronze":
            return "bronze sword"
        if metal_bar == "iron":
            return "iron sword"
        if metal_bar == "steel":
            return "steel sword"
        raise Exception("invalid metal bar")
    except Exception as e:
        print(f"An error occurred: {e}")

#They need to be done 
# do this
try:
    craft_sword("gold bar")
except Exception as e:
    print(e)

#Raise exception practice
def get_player_record(player_id):
    if player_id == 1:
        return {"name": "Slayer", "level": 128}
    if player_id == 2:
        return {"name": "Dorgoth", "level": 300}
    if player_id == 3:
        return {"name": "Saruman", "level": 4000}
    raise Exception("player id not found")

#Different types of exceptions
try:
    10/0
except ZeroDivisionError:
    print("0 division")
except Exception as e:
    print(e)

try:
    nums = [0, 1]
    print(nums[2])
except IndexError:
    print("index error")
except Exception as e:
    print(e)

#Would print
#0 division
#index error

