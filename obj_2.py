#class 를 만들고 이를 객체로 활용하기 위해서는 생성자가 필요하다.
#그러므로 생성자를 만들어 줘야 한다.

class cat:
    #class variable or member
    color = 'red'
    #instance method
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def meow(self):
        print("우리 {}는 색깔이 {}이고 자주 야옹~ 야옹~! 거려요".format(self.name,self.color))

raon = cat('라온','똥')
meon = cat('미용','컬러풀')
raon.meow()
meon.meow()


