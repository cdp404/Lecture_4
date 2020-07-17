class Vector3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({},{},{})'.format(self.x,self.y,self.z)

    def add(self,other):
        return Vector3D(self.x+other.x,self.y+other.y,self.z+other.z)

    def __add__(self,other):
        return Vector3D(self.x+other.x,self.y+other.y,self.z+other.z)

    def mod(self,other):
        return Vector3D(self.x%other.x,self.y%other.y,self.z%other.z)

    def __mod__(self,other):
        return Vector3D(self.x%other.x,self.y%other.y,self.z%other.z)

    def sub(self,other):
        return Vector3D(self.x-other.x,self.y-other.y,self.z-other.z)

    def __sub__(self,other):
        return Vector3D(self.x-other.x,self.y-other.y,self.z-other.z)
