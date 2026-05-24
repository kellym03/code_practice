#Clean code
#Clean Code Does Not:
"""
Make your programs run faster
Make your programs function correctly
Only occur in object-oriented programming
"""
#Clean Code Does:
"""
Make code easier to work with
Make it easier to find and fix bugs
Make the development process faster
Help us retain our sanity
"""

#DRY Code
#don't repeat yourself code

#Classes
#kind of like dictionaries but not, they store name value pairs
# Defines a new class called "Soldier"
# with three properties: health, armor, damage
class Soldier:
    health = 5
    armor = 3
    damage = 2
#Just like a string, integer or float, a class is a type, but instead of being a built-in type, classes are custom types that you define.

#Objects
#So if a class is a new custom type, what's an object? Objects are just instances of a class.

health = 50
# health is an instance of an integer type
aragorn = Soldier()
# aragorn is an instance of the Soldier class type

#The class definition says "hey, I have these specific properties". 
#A dictionary is more powerful in the sense that you can store whatever you want in it, but that also makes it less clear what on earth is in there at any given time.

#Methods
#Classes can have methods! 
# A method is just a function that's tied directly to a class and has access to its properties. See the take_damage method here:

class Soldier:
    health = 5

    # This is a method that reduces the
    # health of the soldier
    def take_damage(self, damage):
        self.health -= damage #need to use the +|-|*|/ = operators in order to apply a method to self

soldier_one = Soldier()
soldier_one.take_damage(2)
print(soldier_one.health)
# prints "3"

soldier_two = Soldier()
soldier_two.take_damage(1)
print(soldier_two.health)
# prints "4"

#Self
#Methods are defined within the class declaration. Their first parameter is always the instance of the class that the method is being called on. 
# By convention, it's called "self", and because self is a reference to the object, you can use it to read and update the properties of the object.
#Notice that methods are called directly on an object instance using the dot operator:

#Method can return
#If a normal function doesn't return anything, it's typically not a very useful function. 
#In contrast, methods often don't return anything because they can mutate (update) the properties of the object instead. '
#'That's exactly what we did in the last assignment.

#However, they can return values if you want! They're just functions with access to an object, after all.
#A common use case is a "getter" method that returns a calculated value based on the properties of the object.

class Soldier:
    armor = 2
    num_weapons = 2

    def get_speed(self):
        speed = 10
        speed -= self.armor
        speed -= self.num_weapons
        return speed

soldier_one = Soldier()
print(soldier_one.get_speed())
# prints "6"

#Methods vs. Functions
#You know what a function is, and a method is the exact same thing, it's just tied directly to a class and has access to the properties of the object.

#A method automagically receives the object it was called on as its first parameter:
class Soldier:
    health = 100

    def take_damage(self, damage, multiplier):
        # "self" is dalinar in the first example
        #
        damage = damage * multiplier
        self.health -= damage

dalinar = Soldier()
# "damage" and "multiplier" are passed explicitly as arguments
# 20 and 2, respectively
# "dalinar" is passed implicitly as the first argument, "self"
dalinar.take_damage(20, 2)
print(dalinar.health)
# 60

adolin = Soldier()
# Again, "adolin" is passed implicitly as the first argument, "self"
# "damage" and "multiplier" are passed explicitly as arguments
adolin.take_damage(10, 3)
print(adolin.health)
# 70

#A method can operate on data that is contained within the class. 
#In other words, you won't always see all the "outputs" in the return statement because the method might just mutate the object's properties directly.

#The OOP Debate
#Because functions are more explicit, some developers argue that functional programming is better than object-oriented programming. 
# Neither paradigm is "better" (I'm required to say this as an educator). The best developers learn and understand both styles and use them as they see fit.

#While methods are more implicit (an object's properties are changed from within), they also make it easier to group a program's data and behavior in one place, which can lead to a more organized codebase. 
# It's tradeoffs all the way down.

#Constructors
#A constructor is (usually) better. It's a specific method on a class called __init__ that is called automatically when you create a new instance of a class.
#So, using a constructor, the code from above would look like this:
class Soldier:
    def __init__(self):
        self.name = "Legolas"
        self.armor = 2
        self.num_weapons = 2

#Not only is this safer (we'll talk about why later), but it also allows us to make the starting property values configurable:
class Soldier:
    def __init__(self, name, armor, num_weapons):
        self.name = name
        self.armor = armor
        self.num_weapons = num_weapons

soldier_one = Soldier("Legolas", 2, 10)
print(soldier_one.name)
# prints "Legolas"
print(soldier_one.armor)
# prints "2"
print(soldier_one.num_weapons)
# prints "10"

soldier_two = Soldier("Gimli", 5, 1)
print(soldier_two.name)
# prints "Gimli"
print(soldier_two.armor)
# prints "5"
print(soldier_two.num_weapons)
# prints "1"

#Class Variables vs. Instance Variables
#We've already worked with both class variables and instance variables, but we haven't really talked about the difference.

#Instance Variables
#Instance variables vary from object to object and are declared in the constructor. They're more common:

class Wall:
    def __init__(self):
        self.height = 10 # instance variable (per object)

south_wall = Wall()
south_wall.height = 20 # only updates this instance of a wall
print(south_wall.height)
# prints "20"

north_wall = Wall()
print(north_wall.height)
# prints "10"

#Class Variables
#Class variables are shared between instances of the same class and are declared at the top level of a class definition. They're less common:
class Wall:
    height = 10 # class variable (shared across all instances)

south_wall = Wall()
print(south_wall.height)
# prints "10"

Wall.height = 20 # updates all instances of a Wall

print(south_wall.height)
# prints "20"

#Which Should I Use?
#Generally speaking, stay away from class variables. 
# Just like global variables, class variables are usually a bad idea because they make it hard to keep track of which parts of your program are making updates. 
# However, it is important to understand how they work because you may see them in the wild.


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        #don't need to self.book since it is already given, doesn't need to be initialised as an instance of the class
        self.books.append(book)
        
    def remove_book(self, book):
        keep_books = []
        for b in self.books:
            if b.title != book.title or b.author != book.author: #using the or logic as only one parameter needs to boolean evaluate to true in order for it to be kept as that means it is different from the book we want to remove
                keep_books.append(b)
        self.books = keep_books

    def search_books(self, search_string):
        matching_books = []
        search_lower = search_string.lower() #lower case everything to prevent case mismatch
        for b in self.books:
            if search_lower in b.title.lower() or search_lower in b.author.lower(): #lower case everything to prevent case mismatch
                matching_books.append(b)
        return matching_books

#Encapsulation
#Encapsulation is the practice of hiding complexity inside a "black box" so that it's easier to focus on the problem at hand.
# E.g. if you provide mass, speed and time you can get acceleration as an output of a function but you don't need to know how the calculation (function) works

#Public and Private
#By default, all properties and methods in a class are public. That means that you can access them with the . operator:
wall.height = 10
print(wall.height)
# 10

#Private data members are a way to encapsulate logic and data within a class definition. 
# To make a property or method private just prefix it with two underscores:

class Wall:
    def __init__(self, armor, magic_resistance):
        self.__armor = armor
        self.__magic_resistance = magic_resistance

    def get_defense(self):
        return self.__armor + self.__magic_resistance

front_wall = Wall(10, 20)

# This results in an error
print(front_wall.__armor)

# This works
print(front_wall.get_defense())
# 30

#We do this to make it easier to use our class. 
# Now when another developer (or even ourselves) use the Wall class, they don't need to think about how armor and magic_resistance affect the defense of a Wall. 
# In fact, we don't even allow them to access armor and magic_resistance directly by making them private with __.

#Encapsulation is not about security in the same way a laptop's casing doesn't stop you from opening it up and looking inside. You can now just find all the workings in one place.

#Encapsulation in Python
#Python is a very dynamic language, which makes it difficult for the interpreter to enforce some of the safeguards that languages like Go do. 
# That's why encapsulation in Python is achieved mostly by convention rather than by force.

#Prefixing methods and properties with a double underscore is a strong suggestion to the users of your class that they shouldn't be touching that stuff. 
# If a developer wants to break convention, there are ways to get around the double underscore rule.

class Wall:
    def __init__(self, height):
        # the double underscore makes this a private property
        # but it's not strictly enforced, there are hacks to get around it
        self.__height = height

    def get_height(self):
        return self.__height
    
#Encapsulation assignment
class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    def cast_fireball(self, target, fireball_cost, fireball_damage):
        if fireball_cost > self.mana:
            raise Exception(f"{self.name} cannot cast fireball")
        else:
            self.mana -= fireball_cost
            target.get_fireballed(fireball_damage)

    def is_alive(self):
        return self.health > 0

    def get_fireballed(self, fireball_damage):
        fireball_damage -= self.__stamina
        self.health -= fireball_damage

    def drink_mana_potion(self, potion_mana):
        potion_mana += self.__intelligence
        self.mana += potion_mana

#Encapsulation practice
class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("cannot deposit zero or negative funds")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("cannot withdraw zero or negative funds")
        if amount > self.__balance:
            raise ValueError("insufficient funds")
        else:
            self.__balance -= amount

#Abstraction vs. Encapsulation
#Abstraction is about creating a simple interface for complex behavior. It focuses on what's exposed (public).
#Encapsulation is about hiding internal state. It focuses on tucking away the implementation details (private).

#Abstraction focuses on exposing essential features while hiding complexity
#Encapsulation focuses on bundling data with methods and restricting direct access to implementation details

#OOP typically groups data and behaviour into a single unit

#Inheritance
#Inheritance allows a "child" class, to inherit properties and methods from a "parent" class. It's a way to share code between classes
class Aircraft:
    def __init__(self, height, speed):
        self.height = height
        self.speed = speed

    def fly_up(self):
        self.height += self.speed

#And say we want to also model more specific kinds of aircraft. We could create a more specific Helicopter class like this:
class Helicopter:
    def __init__(self, height, speed):
        self.height = height
        self.speed = speed
        self.direction = 0

    def fly_up(self):
        self.height += self.speed

    def rotate(self):
        self.direction += 90

#Trouble is, we've rewritten a lot of the same code twice... wouldn't it be nice if a Helicopter could just take all the behavior from an Aircraft, and then just add its own unique behavior on top of that? 
# Well, it can! We'll just make Helicopter a child class of Aircraft:
class Helicopter(Aircraft):
    def __init__(self, height, speed):
        super().__init__(height, speed)
        self.direction = 0

    def rotate(self):
        self.direction += 90

#By adding Aircraft in parentheses after Helicopter, we're saying "make Helicopter a child class of Aircraft". 
# Now Helicopter inherits all the properties and methods of Aircraft!

#The super() method returns a proxy of the parent class, meaning we can use it to call the parent class's constructor and other methods. 
# So the Helicopter's constructor says "first, call the Aircraft constructor, and then additionally set the direction property".

#Now, say we want to create a Jet class. Again, because all jets are aircraft, we can inherit from Aircraft again. 
# One parent class can have as many child classes as you want.

class Jet(Aircraft):
    def __init__(self, speed):
        # Jets always start on the ground
        super().__init__(0, speed)

    def go_supersonic(self):
        self.speed *= 2

#When to inherit
#Inheritance is a powerful tool, but do not overuse it (looking at you, Java devs). The rule of thumb is:
#A should only inherit from B if A is always a B.

#Multiple children
class Hero:
    def __init__(self, name, health):
        self.__name = name
        self.__health = health

    def get_name(self):
        return self.__name

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage


# don't touch above this line


class Archer(Hero):
    def __init__(self, name, health, num_arrows):
        super().__init__(name, health)
        self.__num_arrows = num_arrows

    def shoot(self, target):
        if self.__num_arrows <= 0:
            raise Exception("not enough arrows")
        else:
            self.__num_arrows -= 1
            target.take_damage(10)
        
#Wide not deep
#Why Wide Not Deep?
#A child class is a strict subset of its parent class. 
# In a deep tree, that means the children need to be perfect members of all the parent class "types". That just doesn't happen very often. 
# It's more likely that you'll have a base class that simply has many child classes that are slightly different variations of the base. 
# They're all "siblings" of each other.

#List comprehension in the for loop
def main():
    dragons = [
        Dragon("Green Dragon", 0, 0, 1),
        Dragon("Red Dragon", 2, 2, 2),
        Dragon("Blue Dragon", 4, 3, 3),
        Dragon("Black Dragon", 5, -1, 4),
    ]

    for dragon in dragons:
        print(f"{dragon.name} is at {dragon.pos_x}/{dragon.pos_y}")
    for dragon in dragons:
        opponents = [d for d in dragons if d != dragon] #list comprehension, returns d if logic passes 
        dragon.breathe_fire(3, 3, opponents)

#Polymorphism
#Polymorphism is the ability of a variable, function or object to take on multiple forms.
class Creature():
    def move(self):
        print("the creature moves")

class Dragon(Creature):
    def move(self):
        print("the dragon flies")

class Kraken(Creature):
    def move(self):
        print("the kraken swims")

for creature in [Creature(), Dragon(), Kraken()]:
    creature.move()
# prints:
# the creature moves
# the dragon flies
# the kraken swims

#Because all three classes have a .move() method, we can shove the objects into a single list, and call the same method on each of them, even though the implementation (method body) is different.
class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1 #If it is a private property you need to write getter methods to access them
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

#Overlapping rectangles
#This was hard... I can see why being able to visualise can help
#The below illustrates how there are truthy and falsy values where if there is a true and a false result separated by an OR operator it will evaluate to true
class Rectangle:
    def overlaps(self, rect):
        # They are only separated horizontally if there is an empty gap between them
        separated_x = self.get_right_x() < rect.get_left_x() or self.get_left_x() > rect.get_right_x()
        
        # They are only separated vertically if there is an empty gap between them
        separated_y = self.get_top_y() < rect.get_bottom_y() or self.get_bottom_y() > rect.get_top_y()
        
        # If there is no gap keeping them apart, they are either intersecting or touching!
        return not (separated_x or separated_y)

    # don't touch below this line

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2

    def get_left_x(self):
        return min(self.__x1, self.__x2)

    def get_right_x(self):
        return max(self.__x1, self.__x2)

    def get_top_y(self):
        return max(self.__y1, self.__y2)

    def get_bottom_y(self):
        return min(self.__y1, self.__y2)

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"

#Function signature
#What Is a Function Signature
#A function signature (or method signature) includes the name, inputs, and outputs of a function or method. 
# For example, hit_by_fire in the Human and Archer classes have identical signatures.
class Human:
    def hit_by_fire(self): #name and input
        self.health -= 5
        return self.health #output

class Archer:
    def hit_by_fire(self):
        self.health -= 10
        return self.health
    
#Operator Overloading
#Another kind of built-in polymorphism in Python is the ability to override how an operator works. 
# For example, the + operator works for built-in types like integers and strings.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# TypeError: unsupported operand type(s) for +: 'Point' and 'Point'

#But we can add our own support! Python uses special methods with double underscores, sometimes called "dunder methods", to hook into built-in behaviors. 
# You've already used __init__ to customize how objects are created. 
# If we create an __add__(self, other) method on our class, the Python interpreter will use it when instances of the class are being added with the + operator. 
# The name of the second parameter (other in this example) is just a convention - you can use any valid parameter name. Here's an example:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

p1 = Point(4, 5)
p2 = Point(2, 3)
p3 = p1 + p2
# p3 is (6, 8)

#It is hard coded in the language data model so that __add__ is +

#Operator Overload Review
#As we discussed in the last assignment, operator overloading is the practice of defining custom behavior for standard Python operators. Here's a list of how the operators translate into method names.

"""
Operation	        Operator	       Method
Addition	        +	                __add__
Subtraction	        -	                __sub__
Multiplication	    *	                __mul__
Power	            **	                __pow__
Division	        /	                __truediv__
Floor Division	    //	                __floordiv__
Remainder (modulo)	%	                __mod__
Bitwise Left Shift	<<	                __lshift__
Bitwise Right Shift	>>	                __rshift__
Bitwise AND	        &	                __and__
Bitwise OR	        |	                __or__
Bitwise XOR	        ^	                __xor__
Bitwise NOT	        ~	                __invert__
"""

Overriding Built-In Methods
Last but not least, let's take a look at some of the built-in methods we can override in Python. While there isn't a default behavior for the arithmetic operators like we just saw, there is a default behavior for printing a class instance:
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Point(4, 5)
print(p1)
# <Point object at 0xa0acf8>

#That's not super useful! We probably want to see the fields!

#Let's teach our Point class to print itself. The __str__ method (short for "string") lets us do just that. 
# It takes no inputs but returns a string that will be printed to the console when someone passes an instance of the class to Python's print() function. - hardcoded in

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

p1 = Point(4, 5)
print(p1)
# prints "(4,5)"    

#Boolean Logic operators also work on an index tie breaker basis. For example, below the suit_index will be used as a tie breaker if rank_index is not met
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(self.rank)
        self.suit_index = SUITS.index(self.suit)

    def __eq__(self, other):
        # Compares both values as a pair
        return (self.rank_index, self.suit_index) == (other.rank_index, other.suit_index)

    def __lt__(self, other):
        # Python automatically uses suit_index as a tie-breaker if rank_index matches!
        return (self.rank_index, self.suit_index) < (other.rank_index, other.suit_index)

    def __gt__(self, other):
        return (self.rank_index, self.suit_index) > (other.rank_index, other.suit_index)