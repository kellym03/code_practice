#What Is Functional Programming?
#Functional programming is a style (or "paradigm" if you're pretentious) of programming where we compose functions instead of mutating state (updating the value of variables).

#Functional programming is more about declaring what you want to happen, rather than how you want it to happen.
#Imperative (or procedural) programming declares both the what and the how.

#Example of imperative code:

car = create_car()
car.add_gas(10)
car.clean_windows()

#Example of functional code:

return clean_windows(add_gas(create_car()))

#The important distinction is that in the functional example, we never change the value of the car variable, we just compose functions that return new values, with the outermost function, clean_windows in this case, returning the final result.

#Python is not a great choice for functional programming. 
"""
The most important parts of functional programming can be learned in Python, which include:
- Higher-order functions
- First-class functions
- Pure functions
- Recursion
- Closures
- Currying
"""

#immutable means unchangeable
#mutable code means changeable

#immutable data is easier to work with compared to mutable as you know it hasn't changed
#tuples vs lists
#tuples are immutable, lists are mutable
#You can append to a list, but you can not append to a tuple. 
# You can create a new copy of a tuple using values from an existing tuple, but you can't change the existing tuple.

#Lists are mutable - note the type specifier 'tuple' instead of 'list'
ages: list[int] = [16, 21, 30]
# 'ages' is being changed in place
ages.append(80)
# [16, 21, 30, 80]

#Tuples are immutable - note the type specifier 'tuple' instead of 'list'
ages: tuple[int, ...] = (16, 21, 30)
# note the comma after 80! It's required for a single-element tuple
more_ages: tuple[int, ...] = (80,)
# 'all_ages' is a brand new tuple
all_ages: tuple[int, ...] = ages + more_ages
# (16, 21, 30, 80)

# or we can even reassign the same variable to point to a new tuple:
ages = ages + more_ages
# (16, 21, 30, 80)

def add_prefix(document: str, documents: tuple[str, ...]) -> tuple[str, ...]:
    prefix = f"{len(documents)}. "
    new_doc = prefix + document
    documents.append(new_doc)
    return documents

#Declarative vs Imperative Code
#Declarative is telling the code what you want to happen, while imperative is telling the code how you want it to happen.    
#For example, in CSS it is declarative, you just say "I want this element to be red", but in JavaScript it is imperative, you have to say "find the element, then change its color to red".  

#Declarative code tends to be popular among more mathetical programmers, while imperative code tends to be popular among more procedural programmers.
#An imperative python way of derving the average of a list of numbers might look like the below:
def get_average(nums: list[int]) -> float: #nums is the parameter, and list[int] is the type hint that says nums is a list of integers. The return type hint says that this function returns a float.
    total = 0
    for num in nums:
        total += num
    return total / len(nums)
#A system is described as stateful if it is designed to remember preceding events or user interactions;[1] the remembered information is called the state of the system.

#A more declarative way of doing the same thing would be to use the built-in sum function and the len function:
def get_average(nums: list[int]) -> float:
    return sum(nums) / len(nums)

#Functional programming debugging
def format_line(line: str) -> str:
    return f"{line.rstrip().capitalize().replace(',', '')}...."

#Load up the print statements line by line to debug the function:
def format_line(line: str) -> str:
    formatted = line.strip()
    formatted = formatted.upper()
    formatted = formatted.replace('.','')
    return f"{formatted}..."
    
#Functional vs Object-Oriented Programming
# Of the four pillars of OOP, encapsulation, abstraction and polymorphism are compatible with functional programming. Only inheritance is incompatible with functional programming.    
    
#Statements vs Expressions
# Statements are instructions that do something, while expressions are pieces of code that evaluate to a value.    
#Statement Examples
"""
"Set n to 7"
"Define a function named greet"
"If x > 10, print a greeting to Alice"
"""
n: int = 7  # Variable assignment statement

def greet(name: str) -> str:  # Function definition statement
    return f"Hello, {name}!"

if x > 10:  # `if` statement
    print(greet("Alice"))

for i in range(n):  # `for` loop statement
    print(i)

#Expression
#Expressions are a subset of statements that produce values. 
# Evaluating an expression results in a value that can be used in whatever way is needed. 
# It can be assigned to a variable, returned from a function, etc.

result: int = 2 + 2  # Arithmetic expression
length: int = len("hello")  # Function call expression
total_cost: float = len(items) * cost  # Multiple expressions combined into one

#Expressions Over Statements
#Because expressions always produce values, they're reusable and declarative. You can compose expressions and nest them within each other – but you can't always do that with other kinds of statements.

F#unctional programming encourages the use of expressions over statements where possible, because expressions tend to minimize side effects, and make the code easier to reason about. For example, a function that returns a sum is an expression:

total: int = sum([1, 2, 3, 4])

#We can get the same result with a loop, but that involves a series of statements:

total: int = 0
for n in [1, 2, 3, 4]:
    total += n

#Again, it's simple to combine expressions:

print(sum([1, 2, 3, 4]) * 2)  # 20

#But we can't really do the same thing with our series of statements:

# This doesn't work!
print((
total = 0
for n in [1, 2, 3, 4]:
    total += n
) * 4)

# Expressions always produce a value, which lets you plug one expression into another and reuse the result, making them composable. 
# You also connected functional programming's preference for expressions to minimizing side effects, which makes the code easier to reason about and understand.

#Ternary Expressions
#Originally I might have written this code using an if statement like:
result: float = 0
if number % 2 == 0:
    result = number / 2
else:
    result = (number * 3) + 1

#however, this can be rewritten using a ternary expression, which is more concise and often more readable:
result: float = number / 2 if number % 2 == 0 else (number * 3) + 1

#Note that code avoids mutating the result variable! Ternary expressions are good for maintaining immutability.
#Converted
if file_extension.lower() in ("markdown", "md"):
        return "markdown"
    else:
        return "plaintext"
#to
    return "markdown" if file_extension.lower() in ("markdown", "md") else "plaintext"

#Hexadecimal to RGB colour conversion
#The int function has inbuilt support for converting hexadecimal strings to integers, as you specify the base as the 2nd parameter in the int function which relies on all letters representing the numbers from 10-35. 
#The int function also knows that if you slice off for example, two digits the first digit will be multiplied by 16 to the power of 1 and the second will be multiplied by 16 to the power of 0.
#For example, 4A
#4 * 16^1 = 64
#A * 16^0 = 10
#64 + 10 = 74

#Converter
def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    if not isinstance(hex_color, str) or len(hex_color) != 6: #isinstance can check a data type, in this case we check if hex_color is a string, and we also check if the length of the string is 6 characters long, which is the length of a valid hex color string (without the # symbol).
        raise Exception("not a hex color string")
    
    if is_hexadecimal(hex_color) == True:
        r = int(hex_color[:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:], 16)
        return r, g, b
    elif is_hexadecimal(hex_color) == False:
        raise Exception("not a hex color string")

# Don't edit below this line


def is_hexadecimal(hex_string: str) -> bool:
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False

#functions as variables
#Callable is the type hint for a function. Callable[[int, int], int] means a function that takes two ints as arguments and returns an int.
from collections.abc import Callable

def add(x: int, y: int) -> int:
    return x + y

# assign the function to a new variable
# called `addition`. It behaves the same
# as the original `add` function
addition: Callable[[int, int], int] = add
print(addition(2, 5))
# 7

from collections.abc import Callable


def file_to_prompt(
    file: dict[str, str], to_string: Callable[[dict[str, str]], str]
) -> str:
    return f"""```
{to_string(file)}
```"""

#Anonymous functions
#Lambda functions are anonymous functions, meaning they don't have a name. They're often used for short functions that are used only once, and are not worth giving a name to. They're also often used as arguments to higher-order functions, which are functions that take other functions as arguments.

#Lambda function dictionary example
get_age: Callable[[str], int | str] = lambda name: { #the type hint of the function is just saying that it accepts a string but will return either an int or a string
    "lane": 29,
    "hunter": 69,
    "allan": 17
}.get(name, "not found")
print(get_age("lane"))
# 29

from collections.abc import Callable


def file_type_getter(
    file_extension_tuples: list[tuple[str, list[str]]],
) -> Callable[[str], str]:
    mapping_dict = {}  # Avoid using 'dict' as a variable name since it's a built-in function

    # 1. Cleanly unpack the tuple into the description name and the list of extensions
    for file_type, extensions in file_extension_tuples: #when you know the loop is going to have mutiple values you should use temp values to unpack the values in the loop, this is cleaner than using indices to access the values in the tuple
        # 2. Loop specifically through the list of extensions
        for extension in extensions:
            # 3. Map the extension string directly to its type string
            mapping_dict[extension] = file_type

    print(mapping_dict)

    # 4. Return an inner function (Closure) that takes an extension and looks it up
    return lambda ext: mapping_dict.get(ext, "Unknown")

#How to use
# 1. Define the input argument matching the type hint
media_types = [
    ("Audio", [".mp3", ".wav", ".flac"]),
    ("Video", [".mp4", ".mkv", ".avi"])
]
#In order to use this function you would first initialise with the file_type_getter function with the tuples and then create new variable where you pass in the file extension against the initialised variable containing the tuples,
# 2. Pass the argument to generate your custom lookup function
checker_tool = file_type_getter(media_types)

# 3. Use the generated tool dynamically in your application
print(checker_tool(".wav"))  # Output: Audio
print(checker_tool(".mp4"))  # Output: Video
print(checker_tool(".exe"))  # Output: Unknown

#First Class vs Higher-Order Functions
#First-class function: A function that is treated like any other value
#Higher-order function: A function that accepts another function as an argument or returns a function

#Map
#"Map," "filter," and "reduce" are three commonly used higher-order functions in functional programming.

#In Python, the built-in map function takes a function and an iterable (often a list) as inputs. It returns an iterator that applies the function to every item, yielding the results.
#the below typical code can be transformed to avoid loops and stateful variables:
def square(x: int) -> int:
    return x * x

nums: list[int] = [1, 2, 3, 4, 5]
squared_nums: list[int] = []
for num in nums:
    num_squared: int = square(num)
    squared_nums.append(num_squared)

print(squared_nums)
# [1, 4, 9, 16, 25]

#with map
from collections.abc import Iterator

def square(x: int) -> int:
    return x * x

nums: list[int] = [1, 2, 3, 4, 5]
squared_nums: Iterator[int] = map(square, nums)

print(list(squared_nums))
# [1, 4, 9, 16, 25]
#map() returns a "map object," so the list() type constructor is needed to convert it back into a standard list.

#Filter function
#The filter function is another built-in higher-order function in Python. It takes a function and an iterable as inputs, and returns an iterator that yields only the items for which the function returns True.    
def is_even(x: int) -> bool:
    return x % 2 == 0

numbers: list[int] = [1, 2, 3, 4, 5, 6]
evens: list[int] = list(filter(is_even, numbers))
print(evens)
# [2, 4, 6]

#single line lambda function with filter
def remove_invalid_lines(document: str) -> str:
    return "\n".join(filter(lambda line: line == "" or not line.startswith("-"), document.split("\n")))
#filter requires you to join back together in order to stop it from being a filter object, like a zip object it returns its place in memory
#The lambda function check if the line is empty or starts with '-' and evaluates to True if either conditions are valid and it will apply to the split document. This way it can avoid stateful variables and stay as an expression. 

#functools.reduce
#The reduce function is a bit more complex than map and filter. 
# It takes a function and an iterable as inputs, and returns a single value that is the result of applying the function cumulatively to the items of the iterable, from left to right. 
# The function must take two arguments: the first is the accumulated value so far, and the second is the next item from the iterable.

# import functools from the standard library
import functools

def add(sum_so_far: int, x: int) -> int:
    print(f"sum_so_far: {sum_so_far}, x: {x}")
    return sum_so_far + x

numbers: list[int] = [1, 2, 3, 4]
sum: int = functools.reduce(add, numbers)
# sum_so_far: 1, x: 2
# sum_so_far: 3, x: 3
# sum_so_far: 6, x: 4
# 10 doesn't print, it's just the final result
print(sum)
# 10
#Notice that we're passing the function add without the ()! 
# It means that reduce will take care of execution and pass the parameters for you. 
# Think of passing add like handing someone a recipe (the instructions), instead of the finished dish (the result of the execution).

import functools

def join(doc_so_far: str, sentence: str) -> str:
    return f"{doc_so_far}. {sentence}"

def join_first_sentences(sentences: list[str], n: int) -> str:
    if n == 0:
        return ""
    else:
        return f"{functools.reduce(join, sentences[:n])}."

#The below functions do the same thing, one with loop and one with reduce
def factorial(n: int) -> int:
    # a procedure that continuously multiplies
    # the current result by the next number
    result: int = 1
    for i in range(1, n + 1):
        result *= i
    return result

import functools

def factorial(n: int) -> int:
    return functools.reduce(lambda x, y: x * y, range(1, n + 1))
#This takes x and y as arguments, x is the result of x * y, and y is the next number in the range. If the range was 1 - 5 the final result would be 120 and that is what is returned.

#Zip function

#Practice
def restore_documents(originals: tuple[str, ...], backups: tuple[str, ...]) -> set[str]:
        return set(filter(lambda doc: not doc.isdigit(), map(str.upper, originals + backups)))

#1. Why str.upper and not something.upper()?
#When you use map(), you are not running the function yourself. 
# Instead, you are handing the blueprint of a function over to Python and saying: "Hey, take this machine, walk down the conveyor belt, and pass each item through it for me."
#Because of this, map() requires you to pass the uncalled name of the function (without parentheses ()).
#In Python, str is the name of the built-in string class, and upper is a method belonging to that class. 
# By passing str.upper, you are telling the mapping engine: "Grab the universal upper-case tool built for strings."
#If you had written doc.upper() inside the map directly, Python would try to execute that command immediately right there on that line. 
# But because the variable doc doesn't exist yet outside of a loop or lambda, Python would panic and throw a NameError.

#The word 'doc' is completely arbitrary. It is a temporary variable name chosen purely for readability (short for "document").

#Pure Functions
#If you take nothing else away from this course, please take this: pure functions are fantastic. They have two properties:
#They always return the same value given the same arguments.
#Running them causes no side effects.

#Pure function example
def find_max(nums: list[int]) -> float:
    max_val: float = float("-inf")
    for num in nums:
        if max_val < num:
            max_val = num
    return max_val

#Impure function example
# instead of returning a value
# this function modifies a global variable
global_max: float = float("-inf")

def find_max(nums: list[int]) -> None:
    global global_max
    for num in nums:
        if global_max < num:
            global_max = num


#Reference vs Value
#Reference - The function has access to the original variable, so if it changes the variable, it changes for everyone who has access to that variable.
#Value - The function gets a copy of the variable, so if it changes the variable, it only changes for that function and does not affect the original variable.
#In Python, reference types are; lists, dictionaries, sets, and custom objects. 
#Value types are; integers, floats, strings, booleans and tuples.
#Pass by reference example
def modify_list(inner_lst: list[int]) -> None:
    inner_lst.append(4)
    # the original "outer_lst" is updated
    # because inner_lst is a reference to the original

outer_lst: list[int] = [1, 2, 3]
modify_list(outer_lst)
# outer_lst = [1, 2, 3, 4]

#Pass by value example
def attempt_to_modify(inner_num: int) -> None:
    inner_num += 1
    # the original "outer_num" is not updated
    # because inner_num is a copy of the original

outer_num: int = 1
attempt_to_modify(outer_num)
# outer_num = 1

#In Python, using the assignment operator (=) does not copy the object. It merely creates a new reference pointing to the exact same object in memory.
# The Reference Problem (=)
original = [1, 2, 3]
cloned = original  # Both variables point to the same list

cloned.append(4)
print(original)  # Output: [1, 2, 3, 4] -> Original changed!

# The Solution (.copy())
original = [1, 2, 3]
cloned = original.copy()  # Creates a distinct new list

cloned.append(4)
print(original)  # Output: [1, 2, 3] -> Original remains safe!

#Pure functions are easier to read, easier to reason about, easier to test, and easier to combine. 
# Even if you're working in an imperative language like Python, you can (and should) write pure functions whenever reasonable.

#Input and Output
#examples of input and output
#Reading from or writing to a file on the hard drive
#Accessing the internet
#Reading from or writing to a database
#Even simply printing to the console!!

def convert_case(text: str, target_format: str) -> str: #Make sure the output type hint is correct, in this case it's a string because the function returns a string. Previously it was None, which would cause an error if you tried to return a string from the function.
    if not text or not target_format:
        raise ValueError("no text or target format provided")
    if target_format == "uppercase":
        return text.upper()
    if target_format == "lowercase":
        return text.lower()
    if target_format == "titlecase":
        return text.title()
    raise ValueError(f"unsupported format: {target_format}")

#Functional programmers try to do something called the functional sandwich where the outer layers of the code are impure (handling input and output), but the inner layers are pure (handling the core logic).

#No-op function
#A no-op is an operation that does nothing. It's often used as a placeholder or default function when you want to provide a function argument but don't want it to do anything.
def square(x: int) -> None:
    x * x #This is a no-op because it calculates the square of x but doesn't return it or store it anywhere, so the result is effectively discarded. The function has no side effects and doesn't produce any output, making it a no-op.

#Memoization
#Memoization is a technical term that basically means caching (storing a copy of) the result of a computation so that we don't have to compute it again in the future. For example, take this simple function:
def add(x: int, y: int) -> int:
    return x + y
#A call of add(5, 7) will always evaluate to 12. If you think about it, once we know that add(5, 7) can be replaced with 12, we can just store 12 in memory as the result value. 
# Then, the next time we need to add(5, 7), we can look up the value instead of repeating a (potentially expensive) CPU operation.

#Referential Transparency
#Pure functions are always referentially transparent.
#"Referential transparency" is a fancy way of saying that a function call can be replaced by its would-be return value because it's the same every time. 
# Referentially transparent functions can be safely memoized. For example add(2, 3) can be replaced by the value 5.

#Sorted and the built-in key parameter
#How key Works Generally
#Normally, when Python sorts a collection, it looks directly at the items inside that collection and compares them at face value (e.g., $1 < 2 < 3$ or "Apple" comes before "Banana").
# hen you provide a key function, you are telling Python: "Don't sort the items based on what they look like right now. 
# Instead, pass each item through this function first, look at the result of that function, and sort the items based on those results."

def sort_dates(dates: list[str]) -> list[str]:
    sorted_dates = sorted(dates, key=format_dates)
    return sorted_dates

def format_dates(datestamp: str):
    date_split = datestamp.split("-")
    correct_format = [date_split[2],date_split[0],date_split[1]] #split and rearrange the datestamp from "MM-DD-YYYY" to "YYYY-MM-DD" so that it can be sorted correctly by year, then month, then day.
    return correct_format