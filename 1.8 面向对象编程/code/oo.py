# -*- coding: UTF-8 -*-
 
class Person:
    pass # An empty block
 
p = Person()
print(p)


class Person1:
    def sayHi(self):
        print('Hello, how are you?')
 
p1 = Person1()
p1.sayHi()

class Person2:
    def __init__(self, name):
        self.name = name
    def sayHi(self):
        print('Hello, my name is', self.name)
 
p2 = Person2('玄魂')
p2.sayHi()


 
class Person3:
    '''Represents a person.'''
    population = 0
 
    def __init__(self, name):
        '''Initializes the person's data.'''
        self.name = name
        print( '(Initializing %s)' % self.name)
 
        # When this person is created, he/she
        # adds to the population
        Person3.population += 1

 
    def sayHi(self):
        '''Greeting by the person.
 
        Really, that's all it does.'''
        print('Hi, my name is %s.' % self.name)
 
    def howMany(self):
        '''Prints the current population.'''
        if Person3.population == 1:
            print('I am the only person here.')
        else:
            print('We have %d persons here.' % Person3.population)
 
xh = Person3('玄魂')
xh.sayHi()
xh.howMany()
 
kl = Person3('考拉')
kl.sayHi()
kl.howMany()
 
xh.sayHi()
xh.howMany()

class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: %s)' % self.name)
 
    def tell(self):
        '''Tell my details.'''
        print('Name:"%s" Age:"%s"' % (self.name, self.age))
 
class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print('(Initialized Teacher: %s)' % self.name)
 
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "%d"' % self.salary)
 
class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: %s)' % self.name)
 
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "%d"' % self.marks)
 
t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('xh', 22, 75)
 
print() # prints a blank line
 
members = [t, s]
for member in members:
    member.tell() # works for both Teachers and Students