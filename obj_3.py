class cat:
    #class variable or member (기본값)
    color = 'red'
    sound = '야옹'
    #instance method
    def __init__(self,name,color,sound): # 생성자 == cat()에서 입력받은값 , 받은입력이 없을시 기본값
        self.name = name
        self.color = color
        self.sound = sound
    def meow(self,name,sound): #cat.meow()에서 입력받은 값
        print('우리 고양이는 못생긴 {} 이에요'.format(name))
        print("길냥이 {}는 색깔이 {}이고 자주 {}~ {}~! 거려요".format(self.name,self.color,sound,sound))


gang_cat = cat('미옹','컬러풀','미야옹')
# jong_cat = cat('태경','똥')
gang_cat.meow('라온','미용')
# jong_cat.meow('라온')