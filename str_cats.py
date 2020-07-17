class cat:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def __str__(self):
        return 'cat(name='+self.name+',color='+self.color+')'


nabi = cat('나비','검정색')
nero = cat('네로','흰색')
print(nabi)
print(nero)

a = 11
print('가나다라'+a+'아자')