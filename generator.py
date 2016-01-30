# coding:utf-8
#列表生成式 list Comprehensions
import os
L = [x*x for x in range(10)]
print(L)

print([d for d in os.listdir('.')])

L2 = ["Good","Dota","Gda"]

print([s.lower() for s in L2])

#生成器 generator
g =  (x*x for x in range(10))

for i in range(10):
 print(g.next())

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print(b)
        a,b = b, a+b
        n = n +1

fib(10)

print("generator-----------")

def fib2(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b, a+b
        n = n +1
c = fib2(10)
for i in range(10):
 print(c.next())
