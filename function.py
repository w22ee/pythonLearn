def say_hi():
    print("hi")
say_hi()

def print_sum(a,b):
    c = a + b
    print(c)
print_sum(9,23)

def hello_same(str):
    print("hello "+str +"!")
hello_same("lixi")

def repeat_str(str,times):
    repeat_strs = str* times
    return repeat_strs
print(repeat_str(" lixi learn python",100))

x = 60

def foo(x):
    print("x is " + str(x))
    x = 3
    print("change local x to "+str(x))

foo(x)
print("x out is "+str(x))


def foo():
    global x
    print("x is " + str(x))
    x = 4
    print("change local x to "+str(x))

foo()
print("x out is "+str(x))

def repeat_str(s,times = 1):
    repeat_strs = s * times
    return repeat_strs
print(repeat_str("GTA"))


#keyword

def func(a,b =2 ,c = 4):
    print("a is ", a," and b is ",b ," and c  is ",c)
func(12,17)
func(12,c = 9)
func(a = 60,c = 9)
#func(b = 60,c = 9)

def print_params(fpara,*nums,**wrods):
    print("fpara:"+str(fpara))
    print("nums "+str(nums))
    print("words "+str(wrods))

print_params("hello ",1,2,3,4,word = " words is ",aa  = "aa")