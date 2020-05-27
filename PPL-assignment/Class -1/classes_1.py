from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self):
        self.__eyes = 2
        self.legs = 4
        self.__existence = True
    @abstractmethod
    def sound(self):
        pass
    @abstractmethod
    def color(self):
        pass


class Tiger(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        return "growl"
    def color(self):
        return "orange"
    def show(self):
        print("Tiger")
        print("sound-",self.sound(),"| color-",self.color(),"| legs-",self.legs,"| eyes-",self._Animal__eyes, "| existence-",self._Animal__existence)
        print()

class Lion(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        return "roar"
    def color(self):
        return "yellow"
    def show(self):
        print("Lion")
        print("sound-",self.sound(),"| color-",self.color(),"| legs-",self.legs,"| eyes-",self._Animal__eyes, "| existence-",self._Animal__existence)
        print()

class Zebra(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        return "whinny"
    def color(self):
        return "black -white"
    def show(self):
        print("Zebra")
        print("sound-",self.sound(),"| color-",self.color(),"| legs-",self.legs,"| eyes-",self._Animal__eyes, "| existence-",self._Animal__existence)
        print()

class Monkey(Animal):
    def __init__(self):
        super().__init__()
        self.legs = 2
    def sound(self):
        return "gibber"
    def color(self):
        return "brown golden"
    def show(self):
        print("Monkey")
        print("sound-",self.sound(),"| color-",self.color(),"| legs-",self.legs,"| eyes-",self._Animal__eyes, "| existence-",self._Animal__existence)
        print()

class Horse(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        return "neigh"
    def color(self):
        return "brown"
    def show(self):
        print("Horse")
        print("sound-",self.sound(),"| color-",self.color(),"| legs-",self.legs,"| eyes-",self._Animal__eyes, "| existence-",self._Animal__existence)
        print()

class Hares(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        return "squeak"
    def color(self):
        return  "white"
    def show(self):
        print("hare")
        print("sound-",self.sound(),"| color-",self.color(),"| legs-",self.legs,"| eyes-",self._Animal__eyes, "| existence-",self._Animal__existence)
        print()

class Frogs(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        return  "croak"
    def color(self):
        return  "green"
    def show(self):
        print("Frog")
        print("sound-",self.sound(),"| color-",self.color(),"| legs-",self.legs,"| eyes-",self._Animal__eyes, "| existence-",self._Animal__existence)
        print()

class Fox(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        return "bark"
    def color(self):
        return "brownish red"
    def show(self):
        print("Fox")
        print("sound-",self.sound(),"| color-",self.color(),"| legs-",self.legs,"| eyes-",self._Animal__eyes, "| existence-",self._Animal__existence)
        print()

class Bear(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        return "growl"
    def color(self):
        return "black Or white or brown"
    def show(self):
        print("Bear")
        print("sound-",self.sound(),"| color-",self.color(),"| legs-",self.legs,"| eyes-",self._Animal__eyes, "| existence-",self._Animal__existence)
        print()

class Deer(Animal):
    def __init__(self):
        super().__init__()
    def sound(self):
        return "bell"
    def color(self):
        return "brown"
    def show(self):
        print("Deer")
        print("sound-",self.sound(),"| color-",self.color(),"| legs-",self.legs,"| eyes-",self._Animal__eyes, "| existence-",self._Animal__existence)
        print()




t = Tiger()
t.show()
l = Lion()
l.show()
z = Zebra()
z.show()
m = Monkey()
m.show()
d = Deer()
d.show()
h = Horse()
h.show()
r = Hares()
r.show()
f = Frogs()
f.show()
b = Bear()
b.show()
w = Fox()
w.show()


class Shape(ABC):
    def __init__(self):
        self.regular_shape = True
    @abstractmethod
    def side(self):
        pass
    @abstractmethod
    def angle(self):
        pass

class Triangle(Shape):
    def __init__(self):
        super().__init__()
    def side(self):
        return 3
    def angle(self):
        return 60
    def show(self):
        print("Triangle")
        print("sides-", self.side(),"| angle-",self.angle(),"| regularity-",self.regular_shape)
        print()

class Square(Shape):
    def __init__(self):
        super().__init__()
    def side(self):
        return 4
    def angle(self):
        return 90
    def show(self):
        print("Square")
        print("sides-", self.side(),"| angle-",self.angle(),"| regularity-",self.regular_shape)
        print()

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
    def side(self):
        return 4
    def angle(self):
        return 90
    def show(self):
        print("Rectangle")
        print("sides-", self.side(),"| angle-",self.angle(),"| regularity-",self.regular_shape)
        print()

class Circle(Shape):
    def __init__(self):
        super().__init__()
    def side(self):
        return False
    def angle(self):
        return False
    def show(self):
        print("Circle")
        print("sides-", self.side(),"| angle-",self.angle(),"| regularity-",self.regular_shape)
        print()

class Pentagon(Shape):
    def __init__(self):
        super().__init__()
    def side(self):
        return 5
    def angle(self):
        return  108
    def show(self):
        print("Pentagon")
        print("sides-", self.side(),"| angle-",self.angle(),"| regularity-",self.regular_shape)
        print()

class Hexagon(Shape):
    def __init__(self):
        super().__init__()
    def side(self):
        return 6
    def angle(self):
        return 120
    def show(self):
        print("Hexagon")
        print("sides-", self.side(),"| angle-",self.angle(),"| regularity-",self.regular_shape)
        print()

class Octagon(Shape):
    def __init__(self):
        super().__init__()
    def side(self):
        return 8
    def angle(self):
        return 135
    def show(self):
        print("Octagon")
        print("sides-", self.side(),"| angle-",self.angle(),"| regularity-",self.regular_shape)
        print()

class Ellipse(Shape):
    def __init__(self):
        super().__init__()
    def side(self):
        return False
    def angle(self):
        return False
    def show(self):
        print("Ellipse")
        print("sides-", self.side(),"| angle-",self.angle(),"| regularity-",self.regular_shape)
        print()

class Nonagon(Shape):
    def __init__(self):
        super().__init__()
    def side(self):
        return 9
    def angle(self):
        return 140
    def show(self):
        print("Nonagon")
        print("sides-", self.side(),"| angle-",self.angle(),"| regularity-",self.regular_shape)
        print()

class Heptagon(Shape):
    def __init__(self):
        super().__init__()
    def side(self):
        return 7
    def angle(self):
        return 128.57
    def show(self):
        print("Heptagon")
        print("sides-", self.side(),"| angle-",self.angle(),"| regularity-",self.regular_shape)
        print()

q = Triangle()
q.show()
p = Square()
p.show()
q1 = Circle()
q1.show()
p1 = Rectangle()
p1.show()
q2 = Pentagon()
q2.show()
p2 = Hexagon()
p2.show()
q3 = Heptagon()
q3.show()
p3 = Octagon()
p3.show()
q4 = Nonagon()
q4.show()
p4 = Ellipse()
p4.show()