#클래스를 정의하고 객체를 만드는 방법
#가장기본은 keyword로 class를 사용해서 정의한다.
#self변수 사용하면 instance method라 정의

class cat:
    #class variable or member
    color = 'red'
    #instance method
    def meow(self):
        print("야옹~ 야옹~!")

raon = cat()

raon.meow()
print(raon.color)

