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
