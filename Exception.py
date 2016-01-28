#syntax err
#excpetion
# print(8/0)

# while True:
#     try:
#         x = int(raw_input("input number \n"))
#         break
#     except ValueError:
#         print("not number")


try:
    f = open("runningman1.txt")
    s = f.readline()
    i = int(s.strip())
except IOError as err:
    print("err is {0}".format(err))
except ValueError:
    print("could not convert to an integer")