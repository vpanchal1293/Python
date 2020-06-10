# Literal 9 is an object 
b = 9

# Reference count of object 9 
# becomes 0. 
b = 4

def create_cycle(): 
    # create a list x 
    x = [ ] 

    # A reference cycle is created 
    # here as x contains reference to 
    # to self. 
    x.append(x) 

create_cycle() 

msg = '''
Ways to make an object eligible for garbage collection
'''
print('\n'*2 + msg)
x = [] 
x.append(1) 
x.append(2) 
  
# delete the list from memory or  
# assigning object x to None(Null) 
del x  
# x = None

msg = '''
Automatic Garbage Collection of Cycles
'''
print('\n'*2+msg)
# loading gc 
import gc 
  
# get the current collection  
# thresholds as a tuple 
print("Garbage collection thresholds:", 
                    gc.get_threshold())

msg = '''
Manual Garbage Collection
'''
print('\n'*2+msg)
collected = gc.collect() 
  
# Prints Garbage collector  
# as 0 object 
print("Garbage collector: collected", 
          "%d objects." % collected)


i = 0 
  
# create a cycle and on each iteration x as a dictionary 
# assigned to 1 
def create_cycle(): 
    x = { } 
    x[i+1] = x 
    print x 
  
# lists are cleared whenever a full collection or  
# collection of the highest generation (2) is run 
collected = gc.collect() # or gc.collect(2) 
print "Garbage collector: collected %d objects." % (collected) 
  
print "Creating cycles..."
for i in range(10): 
    create_cycle() 
  
collected = gc.collect() 
  
print "Garbage collector: collected %d objects." % (collected) 
