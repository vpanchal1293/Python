msg = '''
try:
   You do your operations here
   ......................
except ExceptionI:
   If there is ExceptionI, then execute this block.
except ExceptionII:
   If there is ExceptionII, then execute this block.
   ......................
else:
   If there is no exception then execute this block. 
'''
try:
    fh = open("testfile", "r")
    fh.write("This is my test file for exception handling!!")
except IOError:
    print ("Error: can\'t find file or read data")
else:
    print ("Read content in the file successfully")
    fh.close()
    
msg = '''
try:
   You do your operations here
   ......................
except:
   If there is any exception, then execute this block.
   ......................
else:
   If there is no exception then execute this block.
'''
    
msg ='''
try:
   You do your operations here
   ......................
except(Exception1[, Exception2[,...ExceptionN]]]):
   If there is any exception from the given exception list, 
   then execute this block.
   ......................
else:
   If there is no exception then execute this block. 
'''
    
msg = '''
try:
   You do your operations here;
   ......................
   Due to any exception, this may be skipped.
finally:
   This would always be executed.
   ......................
'''
msg = '''
try:
   Business Logic here...
except Exception as e:
   Exception handling here using e.args...
else:
   Rest of the code here...
'''
# Define a function here.
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print ("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz")

msg = '''
Raising an Exception

raise [Exception [, args [, traceback]]]
'''
def functionName( level ):
    if level <1:
        raise Exception(level)
        # The code below to this would not be executed
        # if we raise the exception
        return level

try:
    l = functionName(-10)
    print ("level = ",l)
except Exception as e:
    print ("error in level argument",e.args[0])
    
msg = '''
User-Defined Exceptions
Python also allows you to create your own exceptions by deriving 
classes from the standard built-in exceptions.
'''

class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise Networkerror("Bad hostname")
except Networkerror as e:
    print (e.args)
    

