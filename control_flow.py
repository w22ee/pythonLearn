# coding:utf-8

import  types
# number = 59
# guess = int(input("enter an integer"))
# if guess == number:
#     print("bingo!")
# elif guess < number:
#     print("guess too small")
# else:
#     print("guess too big")
# print("guess is "+str(guess))

#
# for i in range(1,10):
#     print(i)
# else:
#     print("loop is over")
#
# str_list = ["你好","Python","世纪公园",1]
#
# for i in str_list:
#     print(i)
#
# mixed_tuple = (2,0,9,"suber J")
# for i in mixed_tuple:
#     print(i)
#
# phone_book = {"tom":123,"jack":310303,"kim":77,"kim":66}
#
# for i in phone_book:
#     print(i+" = "+ str(phone_book[i]))
#
# for key,elem in phone_book.items():
#     print(key,elem)

number = 59
guess = 0
# while guess != number:
#     guess = int(input("enter an integer"))
#     if guess == number:
#         print("bingo!")
#     elif guess < number:
#         print("guess too small")
#     else:
#         print("guess too big")
# print("guess is "+str(guess))


while True:
    guess = input("enter an integer\n")
    guess = int(guess)
    if guess == number:
        print("bingo!")
        break
    elif guess < number:
        print("guess too small")
        continue
    else:
        print("guess too big")
        continue
print("guess is "+str(guess))

list = [0,1,2]
for i in list:
    if not i:
        continue
    print(i)

list = [0,1,2]
for i in list:
    if not i:
        #有时候需要实现something,但并无卵用
        pass
    print(i)