class Calculator:
    def add(self,a,b):
        print(a+b)
    def sub(self,a,b):
        print(a-b)
    def mul(self,a,b):
        print(a*b)
    def div(self,a,b):
        if b==0:
            print("division by zero")
        else:
            print(a/b)
    def exp(self,a,b):
        print(a**b)
    def fdiv(self,a,b):
        print(a//b)

    def describe(self):
        print("model_num",self.model_num)
        print("made_in",self.made_in)
        print("color",self.color)
        print("discount",self.discount)

c1=Calculator()
c2=Calculator()

c1.model_num="0623"
c1.made_in="India"
c1.color="blue"
c1.discount="9%"

c2.model_num="5544"
c2.made_in="Ireland"
c2.color="olive"
c2.discount="15%"

print("C1 operations and details")
c1.add(6,9)
c1.sub(3,1)
c1.mul(4,5)
c1.div(4,8)
c1.exp(2,3)
c1.fdiv(3,9)
c1.describe()

print("C2 operations and details")
c2.add(12,14)
c2.sub(13,21)
c2.mul(43,56)
c2.div(41,84)
c2.exp(21,9)
c2.fdiv(23,9)
c2.describe()

#what is self?
# self is a conventional name for the first parameter of instance  in a class. 
# It refers to the current instance of the class, allowing access to that specific object's attributes and methods.
# Whenever a method is called via an object, Python automatically passes the object itself as the first argument to the method, which is typically named "self"


