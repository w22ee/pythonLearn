# _*_ coding: utf-8 _*_
print 'hello'
print 'liu shuang', 'is', 'dog', 300, '300+100=', 300 + 100,
print '\njinput name:'
# name = raw_input()
# print 'your input is ',name
age = 14
if age >= 12:
    print('bigger')
else:
    print('smaller')

# a = 'ABC'
# b = a
# a = 'XYZ'
# print b

for i in range(1, 5):
    if i < 3:
        print i
    else:
       break
else:
  print 'end'

p = "lixi"
print('{0} is {1} years old'.format(p,str(age)));
print(p +" is "+ str(age) )
print("你好 \n 中文")
