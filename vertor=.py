class Vector3D:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({},{},{})'.format(self.x,self.y,self.z)

    def eq(self,other):
        if self.x==other.x and self.y==other.y and self.z==other.z:
            print('True')
        else:
            print("False")


    def __eq__(self,other):
        if self.x==other.x and self.y==other.y and self.z==other.z:
            print('True')
        else:
            print("False")

# v1 = Vector3D(10,20,30)
# v2 = Vector3D(10,20,30)
# v3 = Vector3D(11,22,33)
# v1.eq(v2)
# v1 == v3