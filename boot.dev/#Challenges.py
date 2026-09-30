#Challenges
#RPG Damage Analyzer
from functools import reduce

def scale_damage(damages, multiplier):
    return list(map(lambda num: num * multiplier, damages)) #multiplier is already supplied it didn't need to an additional argument for the lambda


def filter_critical_hits(damages, critical_threshold):
    return list(filter(lambda num: num >= critical_threshold, damages)) #filter takes an function, applies it to an iterator (e.g. a list) and then returns and iterator


def total_damage(damages):
    if len(damages) <= 0:
        return 0
    else:
        return reduce(lambda accumulator, num: accumulator + num, damages)

#Compose Shapes with Polymorphism
PI = 3.14159


class Shape:
    def area(self):
        raise NotImplementedError

    def __add__(self, other):
        return CompositeShape([self, other]) #the key lesson is avoid infinite recursion and remembering that __add__ is an existing method that already knows to add and therefore returning the compositeShape object was that was required to add shapes together. The still cofusing part is that you can use a child's method on the parent's object class.

    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (self.radius * self.radius) * PI


class CompositeShape(Shape):
    def __init__(self, shapes):
        self.shapes = shapes

    def area(self):
        shape_area = 0
        for shape in self.shapes:
            shape_area += shape.area()
        return shape_area

    def __add__(self, other):
        return CompositeShape([self, other])

    def __radd__(self, other):
        if other == 0:
            return self
        return NotImplemented
