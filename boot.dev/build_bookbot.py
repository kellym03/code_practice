#built bookbot

#Run Command
#bootdev run 6120f97b-117f-4a84-94d6-a3436f21f1a4

#Submit command
#bootdev run 6120f97b-117f-4a84-94d6-a3436f21f1a4 -s

#Run the CLI commands to test your solution.

#echo "Ready for bookbot"
#Expecting exit code: 0
#Expecting stdout to contain all of:
#Ready for bookbot

#How golang enforced directory creation and code organisation
~/workspace/USERNAME/PROJECTNAME

For example:

~/workspace/bootdotdev/curriculum
~/workspace/wagslane/go-rabbitmq

#Readme
#A README.md is a markdown documentation file that's supposed to explain what your project is and how to run it.
#And if you're a real developer™ then it's always out of date and doesn't provide enough info.

#Get request for Frankenstein book
wget -O books/frankenstein.txt https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/frankenstein.txt

#You need to be in the directory it expects you to be in when you submit in order to not fail the task

#Refactoring
#Refactoring is a fancy word for "rewriting your god-awful code so it's not so terrible." 
# Refactoring doesn't change the behavior of your code, just the way it's written.
#There are different kinds of refactors. The one we're gonna look into is splitting code in one file into smaller modules.

#Importing
#In Python, each .py file is a module, and we can import functions, variables, and classes from one module into another with the import statement. The name of a module is the filename (without the .py extension).
#For example, pretend we had a database.py file with a top-level function called connect and a variable called db_version. We could import those into another file (like a main.py file) like this:

# Import the `connect` function and `db_version` variable from the `database.py` file
from database import connect, db_version

#Or, if we want to import everything from a module, we can use the * character:

# Import everything from the `database.py` file into the current file
from database import *

