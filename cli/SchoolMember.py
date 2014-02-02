class SchoolMember:
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print '(initialized schl members: %s)' %self.name
        
    def tell(self):
        print 'Name: %s, Age: %s' %(self.name, self.age)
        
class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary=salary
        print '(initialized teacher: %s)' %self.name
        
    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: %s' %self.salary
        
class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks=marks
        print '(initialized students: %s)' %self.name
        
    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: %s' %self.marks
        
        
t=Teacher('Mrs. Sola', 40, 30000)
s=Student('adiks', 20, 99)
print 
members=[t, s]
for member in members:
    member.tell()