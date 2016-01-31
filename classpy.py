class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def pInfo(self):
        print(self.name,self.score)



bart = Student("bart",59)
bart.pInfo()