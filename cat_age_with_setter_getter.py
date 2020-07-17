class cat:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return 'cat(name='+self.__name+',age='+str(self.__age)+')'

    def set_age(self,age):
        if age >0:
            self.__age = age
    def get_age(self):
        return self.__age


nabi = cat('나비',3)
print(nabi)
nabi.set_age(4)
nabi.set_age(-5)
print(nabi)

