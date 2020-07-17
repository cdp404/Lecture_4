list_a = [10,20,30]
list_b = [10,20,30]

if list_a is list_b:
    print('list_a is list_b')
else :
    print('list_a is not list_b')

print('list_a 는',id(list_a))
print('list_b 는',id(list_b))

#--------------------------------------

if list_a is not list_b:
    print('list_a is not list_b')
else :
    print('list_a is list_b')
#--------------------------------------
if list_a == list_b:
    print('list_a is list_b')
else :
    print('list_a is not list_b')
#--------------------------------------
num_a = 3
num_b = 3
if num_a is num_b:
    print('num_a is num_b')
else :
    print('num_a is not num_b')
#--------------------------------------
str_a = '안녕'
str_b = '안녕'
if str_a is str_b:
    print('str_a is str_b')
else :
    print('str_a is not str_b')
#--------------------------------------
dic_a = {'a':1,'b':2}
dic_b = {'a':1,'b':2}
if dic_a is dic_b:
    print('dic_a is dic_b')
else :
    print('dic_a is not dic_b')