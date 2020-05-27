from animal import *
from shapes import *  # modularity
t = Tiger()
t.set_limbs(4)
t.show()

m = Man()
m.set_limbs(2, 2)
m.show()


c = Circle()
c.details(True, True)
c.show()

r = Square()
r.details(True)
r.show()
