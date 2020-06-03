class Employee:
    'Common base class for all employees'
    empCount = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)
    
    def displayEmployee(self):
        print ("Name : ", self.name,  ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)

'''
You can add, remove, or modify attributes of classes and objects at any time
'''
Employee.extra_attr = 5
print(Employee.extra_attr)
print (hasattr(Employee ,'extra_attr'))
del Employee.extra_attr
print (hasattr(Employee ,'extra_attr'))


hasattr(emp1, 'salary')    # Returns true if 'salary' attribute exists
getattr(emp1, 'salary')    # Returns value of 'salary' attribute
setattr(emp1, 'salary', 7000) # Set attribute 'salary' at 7000
delattr(emp1, 'salary')    # Delete attribute 'salary'

emp1.salary = 7000  # Add an 'salary' attribute.
emp1.name = 'xyz'  # Modify 'age' attribute.
del emp1.salary  # Delete 'age' attribute.

print(dir(emp1))
print(dir(emp2))
print(dir(Employee))

class basic():
    pass

for attr in dir(basic):
    print(repr(getattr(basic, attr)))

'''
Python deletes unneeded objects (built-in types or class instances)
automatically to free the memory space.
The process by which Python periodically reclaims blocks 
of memory that no longer are in use is termed as Garbage Collection.

Python's garbage collector runs during program execution 
and is triggered when an object's reference count reaches zero. 
An object's reference count changes as the number of aliases that point to it changes.

An object's reference count increases 
when it is assigned a new name or placed in a container (list, tuple, or dictionary).
The object's reference count decreases 
when it is deleted with del, its reference is reassigned, 
or its reference goes out of scope. When an object's reference count reaches zero, 
Python collects it automatically.
'''
class Point:
    def __init__( self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        print('del called')
        class_name = self.__class__.__name__
        print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print (id(pt1), id(pt2), id(pt3))   # prints the ids of the obejcts
del pt1
del pt2
del pt3

class Parent:        # define parent class
    parentAttr = 100
    def __init__(self):
        print ("Calling parent constructor")
    
    def parentMethod(self):
        print ('Calling parent method')
    
    def setAttr(self, attr):
        Parent.parentAttr = attr
    
    def getAttr(self):
        print ("Parent attribute :", Parent.parentAttr)
    
class Child(Parent): # define child class
    def __init__(self):
        print ("Calling child constructor")
    
    def childMethod(self):
        print ('Calling child method')

c = Child()          # instance of child
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method


'''
Function Overloading
'''
class Parent1():        # define parent class
    def myMethod(self):
        print ('Calling parent method')

class Child1(Parent): # define child class
    def myMethod(self):
        print ('Calling child method')

c1 = Child1()          # instance of child
c1.myMethod()         # child calls overridden method

msg = '''
calling parent marthon on child while function ooverloading
'''
print('\n'*3,msg)

class Parent2():        # define parent class
    def myMethod(self):
        print ('Calling parent method')

class Child2(Parent2): # define child class
    def myMethod(self):
        Parent2.myMethod(self)
        print ('Calling child method')

c2 = Child2()          # instance of child
c2.myMethod()         # child calls overridden method


msg = '''
Overloading Operators
'''
print('\n'*3,msg)
class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print (v1 + v2)

msg = '''
Data Hiding
'''
print('\n'*3,msg)


class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print (self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
try:
    print (counter.__secretCount)
except Exception as e:
    print(str(e))
    
msg = '''
Python protects those members by internally 
changing the name to include the class name.
You can access such attributes as object._className__attrName.
If you would replace your last line as following, then it works for you
'''
print('\n'*3,msg)

print (counter._JustCounter__secretCount)