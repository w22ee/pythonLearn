# _*_ coding:utf-8 _*_
#tuple 元素不能更改,其他都和list一样
number_tuple = (1,2,3,4,2,6);
number_list = [1,2,2,3,4]

str_tuple = ("mmm","中文","python tuple")
mixed_tuple = (2,0,9,"suber J")
print("number_tuple is "+str(number_tuple))
print("str_tuple is "+str(str_tuple))
print("mixed_tuple is "+str(mixed_tuple))

# del number_tuple

print("number_tuple *4 is  "+str(number_tuple*4))

a_tuple= (2,["A","b"])

print("a_tuple is "+ str(a_tuple))

a_tuple[1][1] = "fantasy"
print("a_tuple is "+ str(a_tuple))
