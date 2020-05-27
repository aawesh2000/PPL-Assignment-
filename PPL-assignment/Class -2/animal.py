from abc import ABC, abstractmethod

class Animal(ABC):   #abstract class
    def __init__(self):
        self.existence = True
        self.sound = "no"
        self.legs = 4
        self.hands = 0
    
    def set_limbs(self,limbs):
        pass
    
    def get_limbs(self):
        pass

    @abstractmethod
    def type_of_animal(self):
        pass

    

class info(ABC):   #interface class
    @abstractmethod
    def color(self):
        pass



class Tiger(Animal,info): #inheritance
    def __init__(self):
        Animal.__init__(self)
        
        
    def set_limbs(self,limbs):
        self.legs = limbs
        
    def get_limbs(self):
        return self.legs
    
    
    def type_of_animal(self):
        return "carnivorous"

    def color(self):
        return "orange"
    def show(self):
        print("Tiger")
        print("type of animal-",self.type_of_animal(),"|  limbs-",self.get_limbs(),"|  color-",self.color())
        print()

class Lion(Animal,info):
    def __init__(self):
        Animal.__init__(self)
    def set_limbs(self,limbs):
        self.legs = limbs
        
    def get_limbs(self):
        return self.legs
    
    
    def type_of_animal(self):
        return "carnivorous"
    
    def color(self):
        return "yellow"
    def show(self):
        print("Lion")
        print("type of animal-",self.type_of_animal(),"|  limbs-",self.get_limbs(),"|  color-",self.color())
        print()

class Zebra(Animal,info):
    def __init__(self):
        Animal.__init__(self)
        
        
    def set_limbs(self,limbs):
        self.legs = limbs
        
    def get_limbs(self):
        return self.legs
    
    
    def type_of_animal(self):
        return "herbivorous"

    def color(self):
        return "black-white"
    def show(self):
        print("Zebra")
        print("type of animal-",self.type_of_animal(),"|  limbs-",self.get_limbs(),"|  color-",self.color())
        print()

class Monkey(Animal,info):
    def __init__(self):
        Animal.__init__(self)
        
        
    def set_limbs(self,limbs):
        self.legs = limbs
        
    def get_limbs(self):
        return self.legs
    
    
    def type_of_animal(self):
        return "omnivorous"
    
    def color(self):
        return "brown"
    def show(self):
        print("Monkey")
        print("type of animal-",self.type_of_animal(),"|  limbs-",self.get_limbs(),"|  color-",self.color())
        print()

class Man(Animal,info):
    def __init__(self):
        Animal.__init__(self)
        
        
    def set_limbs(self, legs, hands):  #polymorphism
        self.legs = legs
        self.hands = hands
    
    def get_limbs(self):
        return self.hands,self.legs
        
    def type_of_animal(self):
        return "omnivorous"
    def color(self):
        return "variable"
    def show(self):
        print("Man")
        print("type of animal-",self.type_of_animal(),"|  limbs-",self.get_limbs(),"|  color-",self.color())
        print()

class Hares(Animal,info):
    def __init__(self):
        Animal.__init__(self)
        
        
    def set_limbs(self,limbs):
        self.legs = limbs
        
    def get_limbs(self):
        return self.legs
    
    
    
    def type_of_animal(self):
        return "herbivorous"
    def color(self):
        return "white"
    def show(self):
        print("Hare")
        print("type of animal-",self.type_of_animal(),"|  limbs-",self.get_limbs(),"|  color-",self.color())
        print()

class Frogs(Animal,info):
    def __init__(self):
        Animal.__init__(self)
        
        
        
    def set_limbs(self,limbs):
        self.legs = limbs
        
    def get_limbs(self):
        return self.legs
    
    
    def type_of_animal(self):
        return "carnivorous"
    def color(self):
        return "green"
    def show(self):
        print("Frog")
        print("type of animal-",self.type_of_animal(),"|  limbs-",self.get_limbs(),"|  color-",self.color())
        print()

class Fox(Animal,info):
    def __init__(self):
        Animal.__init__(self)
        
        
    def set_limbs(self,limbs):
        self.legs = limbs
        
    def get_limbs(self):
        return self.legs
    
    
    def type_of_animal(self):
        return "carnivorous"
    def color(self):
        return "brownish red"
    def show(self):
        print("Fox")
        print("type of animal-",self.type_of_animal(),"|  limbs-",self.get_limbs(),"|  color-",self.color())
        print()

class Bear(Animal,info):
    def __init__(self):
        Animal.__init__(self)
        
        
    def set_limbs(self,limbs):
        self.legs = limbs
        
    def get_limbs(self):
        return self.legs
    
    
    def type_of_animal(self):
        return "omnivorous"
    def color(self):
        return "brown red white"
    def show(self):
        print("Bear")
        print("type of animal-",self.type_of_animal(),"|  limbs-",self.get_limbs(),"|  color-",self.color())
        print()

class Deer(Animal,info):
    def __init__(self):
        Animal.__init__(self)
        
        
    def set_limbs(self,limbs):
        self.legs = limbs
        
    def get_limbs(self):
        return self.legs
    
    
    def type_of_animal(self):
        return "herbivorous"
    def color(self):
        return "brownish"
    def show(self):
        print("Deer")
        print("type of animal-",self.type_of_animal(),"|  limbs-",self.get_limbs(),"|  color-",self.color())
        print()