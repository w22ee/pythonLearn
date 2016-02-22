
#map
def f(x):
    return x * x
print map(f,[1,2,3,4,5,6])

print map(str,[1,2,3,4,5])


#reduce
def add(x,y):
    return x+y
print reduce(add,[1,2,3,4,5])

nameList = ['lisA','bArT','ADAM','MeGe']

def toLower(name):
    return  name.capitalize()

print map(toLower,nameList)

def prod(intList):
    def mu(x,y):
        return x * y
    return reduce(mu,intList)


print prod([1,2,3,4,5,6])