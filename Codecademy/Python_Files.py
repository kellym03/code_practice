#Python Files

#reading a file
with open("simple_text.txt") as text_file:
  text_data = text_file.read()
print(text_data)

#iterating through a file
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc:
    print(line)

#reading just the first line of a file
with open("just_the_first.txt") as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)

with open("bad_bands.txt", "w") as bad_bands_doc:
  bad_bands_doc.write("Bad band #1")

with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write("Air Buddy\n")

# Old close method for closing a file
fun_cities_file = open('fun_cities.txt', 'a')

# We can now append a line to "fun_cities".
fun_cities_file.write("Montréal")

# But we need to remember to close the file
fun_cities_file.close()

#Reading a csv
with open("logger.csv") as log_csv_file:
  print(log_csv_file.read())

#Reading a csv with the csv module and converting it to a dictionary and printing the "Cool Fact" column
import csv

with open("cool_csv.csv") as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact'])

#Reading a csv with the csv module and converting it to a dictionary and printing the "ISBN" column
import csv
with open("books.csv", newline = '') as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter="@")
  isbn_list = []
  for row in books_reader:
    isbn_list.append(row['ISBN'])
  print(isbn_list)

#Writing a csv with the csv module and a list of dictionaries. The csv will have the fieldnames "time", "address", and "limit". The data is in the list of dictionaries called access_log.
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv
with open("logger.csv", "w") as logger_csv:
  log_writer = csv.DictWriter(logger_csv, fieldnames = fields)
  log_writer.writeheader()
  for dic in access_log:
    log_writer.writerow(dic)
  print(log_writer)

#Reading a json file and printing the value of the "text" key
import json
with open("message.json") as message_json:
  message = json.load(message_json)
  print(message['text']) #remember that json files are key-value pairs and that the input of 'text' is a string key, not a variable or special input

#Writing a json file with the json module and a list of dictionaries. The json file will have the key "interesting message" and the value "What is JSON? A web application's little pile of secrets." and the key "follow up" and the value "But enough talk!".
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]
import json
with open("data.json", 'w') as data_json:
  json.dump(data_payload, data_json)

#Hacking the Fender Project
import csv
with open("passwords.csv") as password_file:
  compromised_users = []
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    #print(password_row['Username'])
    compromised_users.append(password_row['Username'])
  #print(compromised_users)

with open("compromised_users.txt", "w") as compromised_user_file:
  for row in compromised_users:
    compromised_user_file.write(row)

import json
boss_message_dict = {"recipient":"The Boss","message":"Mission success"}
with open("boss_message.json", "w") as boss_message:
  json.dump(boss_message_dict, boss_message)

with open("new_passwords.csv", "w") as new_passwords_obj:
  slash_null_sig = """
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/

  """
  new_passwords_obj.write(slash_null_sig)