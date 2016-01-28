# coding:utf-8
class Student:
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print("I am "+self.name)
        print("my grade is ", self.grade)

    def imrpove(self,amonut):
        self.grade = self.grade + amonut

jim = Student("jim",86)
jim.introduce()
jim.imrpove(10)
jim.introduce()


#可以传入一个函数
# def add_candles(cake_func):
#     def insert_candles():
#         return cake_func + " candles"
#     return insert_candles
#
# def make_cake():
#     return "cake"
#
# gift_func = add_candles(make_cake())
# print(make_cake())
# print(gift_func())

def add_candles(cake_func):
    def insert_candles():
        return cake_func() + " candles"
    return insert_candles

@add_candles
def make_cake():
    return "cake"

# make_cake = add_candles(make_cake())
print(make_cake())