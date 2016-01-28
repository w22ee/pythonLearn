# coding:utf-8
my_book = '''running man ep0231 is verg good
           我喜欢李光洙的表演
           大发'''
f = open("runningman.txt","w")
f.write(my_book)
f.close()


r = open("runningman.txt")
while True:
    line  = r.readline()
    if len(line) == 0:
        break
    print(line)
r.close()