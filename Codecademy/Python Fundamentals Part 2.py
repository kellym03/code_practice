# Codecademy Python Fundamentals Part 2
# Converting JSON to CSV

import requests
import csv

r = requests.get('https://api.census.gov/data/2020/acs/acs5?get=NAME,B08303_001E,B08303_013E&for=county:*&in=state:36')

r_json = r.json()

with open('commute_data.csv', mode='w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(r.json())

# Exploring data using pandas

import pandas

commute_df = pandas.read_csv("commute_data.csv")
print(commute_df.head())

commute_df.columns = ['County', 'All Commuters', 'Commuters > 90min travel', 'state', 'county']

print(commute_df.head())

# Simulating a binomial distribution
import numpy

print(numpy.random.binomial(n = 100, p = 0.8, size=500))

#Escape markers in strings
print("This is a string with a \"double quote\" inside it.")

#strings & conditionals
def letter_check(word, letter):
  letter_exists = False
  for i in word:
    if i == letter:
      letter_exists = True
  return letter_exists
print(letter_check("blue", "b"))

#Strings and Conditionals (Part Two)
def contains(big_string, little_string):
  return little_string in big_string

def common_letters(string_one, string_two):
  common = []
  for letter in string_one:
    if (letter in string_two) and not (letter in common):
      common.append(letter)
  return common

# Review
def username_generator(first_name, last_name):
  user_name = first_name[:3]+last_name[:4]
  return user_name
username_generator("Abe", "Simpson")

def password_generator(user_name):
  #password = user_name[-1]+user_name[:-1]
  password = ""
  for i in range(len(user_name)):
    password += user_name[i-1]
  return password

print(password_generator("AbeSimp"))

#splitting strings
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print(author_names)

author_last_names = []
for name in author_names: #for each name in the list of author_names, do the following:
  author_last_names.append(name.split()[-1]) #[-1] means the last element in the list, which is the last name

print(author_last_names)

#Joining strings
#The string .join() acts on is the delimiter you want to join with, therefore the list you want to join has to be the argument.
my_munequita = ['My', 'Spanish', 'Harlem', 'Mona', 'Lisa']
print(' '.join(my_munequita))
# => 'My Spanish Harlem Mona Lisa'

winter_trees_full = "\n".join(winter_trees_lines) #\n is the newline character, so this will join the lines with a newline in between each line.
print(winter_trees_full)

#Finding the index of a substring
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")
print(disown_placement)

#String formatting with .format(). The curly braces {} are placeholders for the values that will be passed to the .format() method. The order of the values in the .format() method corresponds to the order of the placeholders in the string.
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc

author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(publishing_date, author, title, original_work)

print(my_beard_description)

# Summary project of string manipulation and formatting
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

#print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(",")
#print(highlighted_poems_list)

highlighted_poems_stripped = []
for item in highlighted_poems_list:
  highlighted_poems_stripped.append(item.strip())

#print(highlighted_poems_stripped)

highlighted_poems_details = []
for detail in highlighted_poems_stripped:
  highlighted_poems_details.append(detail.split(":"))
#print(highlighted_poems_details)

titles = []
poets = []
dates = []

for detail in highlighted_poems_details:
  titles.append(detail[0])
for detail in highlighted_poems_details:
  poets.append(detail[1])
for detail in highlighted_poems_details:
  dates.append(detail[2])

print(titles)
print(poets)
print(dates)

#because indexing is used default values are placed within the curly braces in the .format() method, therefore the order of the values in the .format() method corresponds to the order of the placeholders in the string.
for i in range(len(highlighted_poems_details)):
  print("The poem {} was published by {} in {}.".format(titles[i], poets[i], dates[i]))

  #Python Strings: Medical Insurance Project
  medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

# Add your code here
#print(medical_data)
updated_medical_data = medical_data.replace("#", "$")
#print(updated_medical_data)
num_records = 0
for i in updated_medical_data:
  #print(i)
  if i == "$":
    num_records += 3
print(f"There are {num_records} medical records in the data.")
medical_data_split = updated_medical_data.split(";")
#print(medical_data_split)
medical_records = []
for record in medical_data_split:
  medical_records.append(record.split(","))
#print(medical_records)

medical_records_clean = []
for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)
#print(medical_records_clean)

for record in medical_records_clean:
  record[0] = record[0].upper()

print(medical_records_clean)

names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
  names.append(record[0])
for record in medical_records_clean:
  ages.append(record[1])
for record in medical_records_clean:
  bmis.append(record[2])
for record in medical_records_clean:
  insurance_costs.append(record[3])

print(names)
print(ages)
print(bmis)
print(insurance_costs)

total_bmi = 0
for bmi in bmis:
  total_bmi += float(bmi)
#print(total_bmi)
average_bmi = round(total_bmi / len(bmis), 2)
print(f"Average BMI: {average_bmi}")

insurance_costs_float = []
for record in insurance_costs:
  insurance_costs_float.append(record.replace("$",""))
#print(insurance_costs_float)

total_insurance_costs = 0
for record in insurance_costs_float:
  total_insurance_costs += float(record)
#print(total_insurance_costs)
average_insurance_cost = total_insurance_costs / len(insurance_costs_float)
print(f"The average insurance cost is: {average_insurance_cost}")

for i in range(len(medical_records_clean)):
  print(f"{names[i]} is {ages[i]} years old with a BMI of {bmis[i]} and an insurance cost of ${insurance_costs[i]}")

#Coded Correspondence
#Decodding a message
def caesar_decode(text, offset):
    decoded_message = ""
    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            start = ord('a') if char.islower() else ord('A')
            # Shift the character forward by the offset and wrap using modulo 26
            decoded_char = chr((ord(char) - start + offset) % 26 + start)
            decoded_message += decoded_char
        else:
            # Keep spaces and punctuation unchanged
            decoded_message += char
    return decoded_message

# Your cipher text
cipher_text = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"

# Decoding with an offset of 10
decoded_result = caesar_decode(cipher_text, 10)

print(f"Decoded Message: {decoded_result}")

print(5 % 5)

#Encoding a message
def caesar_encode(text, offset):
  encoded_message = ""
  for char in text:
    if char.isalpha():
      # Determine if the character is uppercase or lowercase
      start = ord('a') if char.islower() else ord('A')
      # Shift the character forward by the offset and wrap using modulo 26
      encoded_char = chr((ord(char) - start + offset) % 26 + start)
      encoded_message += encoded_char
    else:
      # Keep spaces and punctuation unchanged
      encoded_message += char
  return encoded_message

encode_text = "Hi Vishal, that was too easy! Let's try something harder next time."

encoded_result = caesar_encode(encode_text, 10)

print(f"Encoded Message: {encoded_result}")

#Double decode
message_one = "jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud."
message_two = "bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!"

message_one_decoded = caesar_decode(message_one, 10)
message_two_decoded = caesar_decode(message_two, 14)

print(message_one_decoded)
print(message_two_decoded)

#No shift key provided, so we can use brute force to try all possible shifts and see which one makes sense.
brute_force_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
brute_force_message_decoded = caesar_decode(brute_force_message, 7)
print(brute_force_message_decoded)

#Vigenere Cipher decoder and encoder
def vigenere_decode(message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    decoded_message = ""
    keyword_index = 0
    
    for char in message:
        if char in alphabet:
            char_index = alphabet.find(char)
            key_char = keyword[keyword_index % len(keyword)]
            key_index = alphabet.find(key_char)
            
            # CHANGE: Use PLUS here because the original message was 
            # encoded by shifting backwards.
            original_index = (char_index + key_index) % 26
            decoded_message += alphabet[original_index]
            
            keyword_index += 1
        else:
            decoded_message += char
            
    return decoded_message

message = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztylktoikqq!"
keyword = "friends"

print(vigenere_decode(message, keyword))

def vigenere_encode(message, keyword):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encoded_message = ""
    keyword_index = 0
    
    for char in message:
        # Convert to lowercase to match our alphabet string
        lower_char = char.lower()
        
        if lower_char in alphabet:
            char_index = alphabet.find(lower_char)
            
            # Get the index of the current keyword character
            key_char = keyword[keyword_index % len(keyword)].lower()
            key_index = alphabet.find(key_char)
            
            # SUBTRACT to encode (reversing the 'decode' logic)
            # % 26 ensures that if we get a negative number, it wraps to the end of the alphabet
            new_index = (char_index - key_index) % 26
            
            # Preserve the original case
            if char.isupper():
                encoded_message += alphabet[new_index].upper()
            else:
                encoded_message += alphabet[new_index]
            
            # Increment keyword index only when we process a letter
            keyword_index += 1
        else:
            # Keep spaces and punctuation as they are
            encoded_message += char
            
    return encoded_message

# Let's test it out!
my_secret = "thanks for the help gemini!"
my_key = "friends"

print(vigenere_encode(my_secret, my_key))

#Dictionaries
#Dictonaries - lists and dictionaries cannot be a key in a dictionary because they are mutable, meaning they can be changed after they are created. This would cause issues with the integrity of the dictionary, as the key could change and the value would no longer be accessible.
#Below is how you can add a new key-value pair to a dictionary using square bracket notation.
user_ids[test] = 12345
#The below is how you can update a dictionary with new key-value pairs using the .update() method.
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper":138475,"stringQueen":85739})
print(user_ids)
# This returns {'teraCoder': 9018293, 'proProgrammer': 119238, 'theLooper': 138475, 'stringQueen': 85739}

#Dictionary Comprehension
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {drinks:caffeine for drinks, caffeine in zipped_drinks}

print(drinks_to_caffeine)

#.get() method for dictionaries. 
# The .get() method returns the value for the specified key if the key is in the dictionary, otherwise it returns the default value provided as the second argument (or None if no default is provided).
inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
print(inventory.get("stone glove", 30)) #returns 20 because "stone glove" is a key in the inventory dictionary and its value is 20


#Deleting a key with .pop() method. The .pop() method removes the specified key and returns the corresponding value. 
# If the key is not found, it returns the default value provided as the second argument (or raises a KeyError if no default is provided).
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

if "stamina grains" in available_items: #if you want to do an item check manually however the .pop() method can also be used to check for the item and remove it in one step, as shown in the next code block without throwing an error
  health_points += available_items["stamina grains"]
  available_items.pop("stamina grains", 0)
  print(health_points)
print(available_items)

health_points += available_items.pop("power stew", 0)
print(health_points)
print(available_items)

health_points += available_items.pop("mystic bread", 0)
print(health_points)
print(available_items)

#Get a list of the keys in a dictionary
#We want to get a roster of the students in the class, without including their grades. We can do this with the built-in list() function:

test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

print(list(test_scores))
# Prints ["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]

#Dictionaries also have a .keys() method that returns a dict_keys object. 
# A dict_keys object is a view object, which provides a look at the current state of the dictionary, without the user being able to modify anything. 
# The dict_keys object returned by .keys() is a set of the keys in the dictionary. 
# You cannot add or remove elements from a dict_keys object, but it can be used in the place of a list for iteration:

for student in test_scores.keys():
 print(student)

#will yield:
Grace
Jeffrey
Sylvia
Pedro
Martin
Dina

#The below code will print dict_keys object
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
print(users)
lessons = num_exercises.keys()
print(lessons)

"""dict_keys(['teraCoder', 'pythonGuy', 'samTheJavaMaam', 'lyleLoop', 'keysmithKeith'])
dict_keys(['functions', 'syntax', 'control flow', 'loops', 'lists', 'classes', 'dictionaries'])"""

#Accessing values in a dictionary. 
# You need to tell the variable in the for loop to focus on the values of the dictionary instead of the keys. 
# You can do this with the .values() method, which returns a dict_values object, which is a view object that provides a look at the current state of the dictionary, without the user being able to modify anything. 
# The dict_values object returned by .values() is a list of the values in the dictionary. 
# You cannot add or remove elements from a dict_values object, but it can be used in the place of a list for iteration:

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0
for exercises in num_exercises.values():
  total_exercises += exercises

print(total_exercises)

#Similarly, you can use the .items() method to get a dict_items object, which is a view object that provides a look at the current state of the dictionary, without the user being able to modify anything.
# The dict_items object returned by .items() is a list of tuples, where each tuple is a key-value pair from the dictionary.
# You can use this in a for loop to access both the keys and values at the same time but again in the for loop you need to tell the variable to focus on the key and value of the dictionary instead of just the key or just the value.
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for key, value in pct_women_in_occupation.items():
  print(f"Women make up {value} percent of {key}s.")

#Dictionaries - Tarot Card Project.
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}
spread["past"] = tarot.pop(13)
print(spread)
spread["present"] = tarot.pop(22)
print(spread)
spread["future"] = tarot.pop(10)
print(spread)

for key, value in spread.items():
  print(f"Your {key} is the {value} card.")

#Probability
