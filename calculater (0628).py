x= 0
y= 0
class Calc :
    def __init__(self) :
        self.x = 0
        self.y = 0
        self.result = 0

    def plus(self, x, y) :
        self.result = x+y
        return self.result

    def sub(self, x, y) :
        result = x-y
        return result

    def mul(self, x, y) :
        result = x*y
        return result

    def div(self, x, y) :
        result = x/y
        return result

c=Calc()

r=c.sub(10,20)
print(r)

r=c.plus(10,20)
print(r)

#r=plus(10,20)

