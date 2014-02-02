class Robot:
    population=0
    def __init__(self, name):
        self.name=name
        print '(initializin %s)' %self.name
        Robot.population+=1
        
    def __del__(self):
        print '%s is being destroyed!' %self.name
        Robot.population-=1
        if Robot.population==0:
            print '%s was d last one.' %self.name
        else:
            print 'there ar stil %d robots workin' %Robot.population
            
    def sayHi(self):
        print 'greetings, my masters cal me %s.' %self.name
        
    def howMany():
        print 'we have %d robots\n' %Robot.population
    howMany=staticmethod(howMany)
    
droid1=Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2=Robot('C-3P0')
droid2.sayHi()
Robot.howMany()

print '\nRobots can do some work here.....\n'

print 'robots av finished dr work, so lets destroy dem'

del droid1
del droid2

Robot.howMany()