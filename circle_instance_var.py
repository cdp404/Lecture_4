import math
class Circle:
    def __init__(self,name,radius,PI):
        self.name = name
        self.radius = radius
        self.PI = PI

    def area(self):
        return self.radius**2 * self.PI

    def __del__(self):
        pass

c1 = Circle('원',8,math.tau/2)
# Tau = PI x 2
print(c1.area())

print(c1.__dict__)