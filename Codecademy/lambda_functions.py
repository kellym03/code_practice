#lambda functions
def square(x): 

    return x ** 2 

# Lambda function 

square_lambda = lambda x: x ** 2 

# Basic syntax

lambda [arguments]: [expression] 

# Lambda function to add two numbers 

add = lambda a, b: a + b 

print(add(3, 5))  # Output: 8 

  

# Lambda function to print a name 

greeting = lambda name: f"Hello, {name}!" 

print(greeting("Alice"))  # Output: Hello, Alice! 

#The map() function applies the given lambda function to each item in a list:

numbers = [1, 2, 3, 4, 5] 

squared = list(map(lambda x: x ** 2, numbers)) 

print(squared)  # Output: [1, 4, 9, 16, 25] 

#The filter() function creates a new list of elements for which the given lambda function returns True:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 

even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) 

print(even_numbers)  # Output: [2, 4, 6, 8, 10] 

#The sorted() function can use a lambda function as a key for custom sorting:

students = [('Alice', 'A', 15), ('Bob', 'B', 12), ('Charlie', 'A', 20)] 

sorted_students = sorted(students, key=lambda x: x[2]) 

print(sorted_students) 

# Output: [('Bob', 'B', 12), ('Alice', 'A', 15), ('Charlie', 'A', 20)] 

"""
Advantages and Limitations
Lambda functions offer several advantages:

They are concise and can make code more readable for simple operations.

They’re convenient for small, throwaway functions, especially as arguments to higher-order functions.

However, they also have limitations:

They can only contain expressions, not statements.

They are limited to a single expression, which can make complex operations difficult.

They can be harder to debug due to their anonymous nature.

Best Practices
Use lambda functions when:

You need a simple function for a short period.

You’re passing a simple function as an argument to higher-order functions.

Avoid lambda functions when:

The operation is complex or requires multiple expressions.

You need to reuse the function multiple times (define a regular function instead).

When lambda functions become too complex, it’s often better to use a regular function defined with def. This improves readability and makes your code easier to maintain.

Wrapping Up
Lambda functions are a powerful feature in Python that allow you to write more concise and functional code. They’re particularly useful for simple operations and as arguments to higher-order functions. However, it’s important to use them judiciously and switch to regular functions when the logic becomes more complex.

Practice using lambda functions in your code to become more comfortable with them. Try rewriting some of your existing functions as lambda functions where appropriate, and experiment with using them in map(), filter(), and sorted().

Happy coding!

Test Your Understanding
Try some of these assessments to make sure you know lambda functions!
Fill in the blank
Questions
Fill in the blank below to complete the statement.

Code
Lambda functions in Python are also known as blank 1 functions. 

Answer Choices
quick
temporary
inline
anonymous
Click or drag and drop to fill in the blank

Fill in the blank
Questions
Fill in the blank below to complete the statement.

Code
The basic syntax of a lambda function is: lambda blank 1: expression 
Answer Choices
inputs
arguments
parameters
variables
Click or drag and drop to fill in the blank

Fill in the blank
Questions
Fill in the blank below to complete the statement.

Code
Lambda functions are particularly useful when used with higher-order functions like map(), filter(), and blank 1(). 
Answer Choices
transform
reduce
sorted
apply
Click or drag and drop to fill in the blank


Now Try It Out
Coding question
Questions
Take a look at the following code and play around with it to get a better understanding of lambda functions.
"""

# Come bac to learning about the map function https://www.codecademy.com/paths/data-engineer/tracks/decp-python-fundamentals-for-data-engineers/modules/learn-python3-functions/articles/map-functions