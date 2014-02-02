#
#this is a class with function
#to solve any equation with
#one variable
#USAGE:
#newfunc=func(y='eqn of x')
#f=newfunc.compute
#f(x=constant value)
#
#to set decimal place,
#use newfunc.setdp(no of dp)
#
#watch out for functions wit
#adjustable number of
#variables . . . . .
#

class func(object):
    def __init__(self, y='x'):
        self.y=y
        self.dp="%0.3f"
        
    def setdp(self, n):
        self.dp="%"+str(n/10.)+"f"
    
    def compute(self, x=0):
        return float(self.dp %eval(self.y))