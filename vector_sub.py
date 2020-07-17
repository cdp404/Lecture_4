class Vector3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({},{},{})'.format(self.x,self.y,self.z)

    def sub(self,other):
        return Vector3D(self.x-other.x,self.y-other.y,self.z-other.z)

    def __sub__(self,other):
        return Vector3D(self.x-other.x,self.y-other.y,self.z-other.z)


# v1 = Vector3D(10,20,30)
# v2 = Vector3D(10,20,30)
# v3 = v1.sub(v2)        # sub
# v4 = v1-v2            # __sub__(특수 Method)
# print(v3)
# print(v4)
