# _*_ coding: utf-8 _*_
number_list = [1,2,2,3,4]
number_list2 = [6,1,2,2,0,3,4,5]
print("list = "+str(number_list))
str_list = ["你好","Python","世纪公园",1]
print("list = " +  str(str_list[0]))
print("str max is "+max(str_list))
del str_list[0]
del str_list[1]
print("list == " + str(str_list))

print(number_list[-2])
print(number_list[1:])
print(number_list[2:4])
print(cmp(number_list,number_list2))
print("max is "+str(max(number_list))+" min is "+str(min(number_list))+" len is "+str(len(number_list)))
number_list.extend(number_list2)
number_list.append(19)
number_list.remove(3)
number_list.pop(-4)
number_list2.reverse()
print(str(number_list)+" count 2 times = "+str(number_list.count(2))+ " 2 index is "+ str(number_list.index(2)))
print("number list2 ="+str(number_list2))
number_list2.sort()
print("number list2 ="+str(number_list2))