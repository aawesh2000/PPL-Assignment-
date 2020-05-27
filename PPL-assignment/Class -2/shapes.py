from abc import ABC, abstractmethod


class Shape(ABC):  # abstract class
    def __init__(self):
        self.regular = True
        self.curve = False

    def details(self):
        pass

    @abstractmethod
    def get_angle(self):
        pass


class info(ABC):  # interface class
    

    @abstractmethod
    def get_side(self):
        pass


class Triangle(Shape, info):  # inheritance
    def __init__(self):
        Shape.__init__(self)

    def get_side(self):
        return 3

    def get_angle(self):
        return 60
    
    
    def details(self,regular):
        self.regular = regular
        
    def get_details(self):
        if(self.regular == False):
            return "not regular"
        else:
            return "regular"
        

    def show(self):
        print("Triangle")
        print("sides-", self.get_side(), "| angle-", self.get_angle(),
              "| regularity-", self.get_details())
        print()


class Square(Shape, info):
    def __init__(self):
        Shape.__init__(self)


    def get_side(self):
        return 4

    def get_angle(self):
        return 90
    
    def details(self, regular):
        self.regular = regular

    def get_details(self):
        if(self.regular == False):
            return "not regular"
        else:
            return "regular"

    def show(self):
        print("Square")
        print("sides-", self.get_side(), "| angle-", self.get_angle(),
              "| regularity-", self.get_details())
        print()


class Rectangle(Shape, info):
    def __init__(self):
        Shape.__init__(self)

    def get_side(self):
        return 4

    def get_angle(self):
        return 90
    
    def details(self, regular):
        self.regular = regular

    def get_details(self):
        if(self.regular == False):
            return "not regular"
        else:
            return "regular"

    def show(self):
        print("Rectangle")
        print("sides-", self.get_side(), "| angle-", self.get_angle(),
              "| regularity-", self.get_details())
        print()


class Circle(Shape, info):
    def __init__(self):
        Shape.__init__(self)

    def get_side(self):
        return False

    def get_angle(self):
        return False

    def details(self, regular, curve): #polymorphism
        self.regular = regular
        self.curve = curve
        
    def get_details(self):
        if(self.regular == False and self.curve == False):
            return "not regular and not curve"
        elif(self.regular == True and self.curve == False):
            return "regular but not curve"
        else:
            return "regular and curve"
    
    def show(self):
        print("Circle")
        print("sides-", self.get_side(), "| angle-", self.get_angle(),
              "| regularity-", self.get_details())
        print()


class Pentagon(Shape, info):
    def __init__(self):
        Shape.__init__(self)
        

    def get_side(self):
        return 5

    def get_angle(self):
        return 108

    def details(self, regular):
        self.regular = regular

    def get_details(self):
        if(self.regular == False):
            return "not regular"
        else:
            return "regular"
    
    def show(self):
        print("Pentagon")
        print("sides-", self.get_side(), "| angle-", self.get_angle(),
              "| regularity-", self.get_details())
        print()


class Hexagon(Shape, info):
    def __init__(self):
        Shape.__init__(self)
        

    def get_side(self):
        return 6

    def get_angle(self):
        return 120
    
    def details(self, regular):
        self.regular = regular

    def get_details(self):
        if(self.regular == False):
            return "not regular"
        else:
            return "regular"

    def show(self):
        print("Hexagon")
        print("sides-", self.get_side(), "| angle-", self.get_angle(),
              "| regularity-", self.get_detail())
        print()


class Octagon(Shape, info):
    def __init__(self):
        Shape.__init__(self)
    

    def get_side(self):
        return 8

    def get_angle(self):
        return 135
    
    def details(self, regular):
        self.regular = regular

    def get_details(self):
        if(self.regular == False):
            return "not regular"
        else:
            return "regular"

    def show(self):
        print("Octagon")
        print("sides-", self.get_side(), "| angle-", self.get_angle(),
              "| regularity-", self.get_details())
        print()


class Ellipse(Shape, info):
    def __init__(self):
        Shape.__init__(self)
        

    def get_side(self):
        return False

    def get_angle(self):
        return False
    
    
    
    def details(self, regular, curve):
        self.regular = regular
        self.curve = curve
        
    def get_details(self):
        if(self.regular == False and self.curve == False):
            return "not regular and not curve"
        elif(self.regular == True and self.curve == False):
            return "regular but not curve"
        else:
            return "regular and curve"

    def show(self):
        print("Ellipse")
        print("sides-", self.get_side(), "| angle-", self.get_angle(),
              "| regularity-", self.get_details())
        print()


class Nonagon(Shape, info):
    def __init__(self):
        Shape.__init__(self)
        
    def get_side(self):
        return 9

    def get_angle(self):
        return 140

    def details(self, regular):
        self.regular = regular

    def get_details(self):
        if(self.regular == False):
            return "not regular"
        else:
            return "regular"

    def show(self):
        print("Nonagon")
        print("sides-", self.get_side(), "| angle-", self.get_angle(),
              "| regularity-", self.get_details())
        print()


class Heptagon(Shape, info):
    def __init__(self):
        Shape.__init__(self)
        

    def get_side(self):
        return 7

    def get_angle(self):
        return 128.57

    def details(self, regular):
        self.regular = regular

    def get_details(self):
        if(self.regular == False):
            return "not regular"
        else:
            return "regular"
    
    def show(self):
        print("Heptagon")
        print("sides-", self.get_side(), "| angle-", self.get_angle(),
              "| regularity-", self.get_details())
        print()
