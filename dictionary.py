# _*_ coding:utf-8 _*_

phone_book = {"tom":123,"jack":310303,"kim":77}
mix_dict = {"tom":"bu leg","jack":310303,"kim":77}

phone_book["tom"] = 4241847

phone_book["liling"] = 183

print(str(phone_book["tom"]))
print(str(phone_book))
del phone_book["kim"]
print(str(phone_book))
phone_book.clear()
print(str(phone_book))
phone_book = {"tom":123,"jack":310303,"kim":77,"kim":66}
print(str(phone_book))

#key可以是数字,字符串,元组不能用list

list_dict = {("name"):"jon","age":13}
print(str(list_dict))

# list_dict = {(["name"],):"jon","age":13}
# print(str(list_dict))

