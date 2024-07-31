class Math:
    def __init__(self,num):
        self.num = num
    def addtonum(self,n):
        self.num = self.num+n
        return self.num
    @staticmethod
    def Add(a,b):
        return a+b

a = Math(5)
print(a.addtonum(3))
result = Math.Add(1,2)
print(result)