
msg = '''
def functionname( parameters ):
   "function_docstring"
   function_suite
   return [expression]

'''
print(msg)


msg = '''
All parameters (arguments) in the Python language are passed by reference.
It means if you change what a parameter refers to within a function
the change also reflects back in the calling function(if assignment is not done in function)
'''
print('\n'*2,msg)
def changeme( mylist ):
    "This changes a passed list into this function"
    print ("Values inside the function before change: ", mylist)
    
    mylist[2]=50
    print ("Values inside the function after change: ", mylist)
    return

mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)

msg = '''
The parameter mylist is local to the function changeme.
Changing mylist within the function does not affect mylist.
The function accomplishes nothing and finally this would produce the following result'''
print('\n'*2,msg)
def changeme2( mylist ):
    "This changes a passed list into this function"
    mylist = [1,2,3,4] # This would assi new reference in mylist
    print ("Values inside the function: ", mylist)
    return

# Now you can call changeme function
mylist = [10,20,30]
changeme2( mylist )
print ("Values outside the function: ", mylist)

msg = '''
variable length agrument
foo(*args) meaning = comma will devide the element
function call foo(1,2,3) --> args = (1,2,3)  -->args[0] = 1, args[1] = 2, args[2] = 3,
function call foo([1,2,3]) --> args = ([1,2,3])  -->  args[0] = [1,2,3]
'''
print('\n'*2,msg)

def printinfo( arg1, *vartuple ):
    "This prints a variable passed arguments"
    print ("Output is: ")
    print ('arg1',arg1)
    print('vartuple',vartuple)
    for var in vartuple:
        print (var)
    return

printinfo( 10 )
printinfo( 70, 60, 50 )


msg = '''keyword argument'''
print('\n'*2,msg)
def myFun(**kwargs):
    print('kwargs=',kwargs)
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 

# Driver code 

myFun(first ='Geeks', mid ='for', last='Geeks')     


msg = '''Using *args and **kwargs to call a function
'''
print('\n'*2,msg)
def myFun2(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3) 
    
# Now we can use *args or **kwargs to 
# pass arguments to this function : 
args = ("Geeks", "for", "Geeks") 
myFun2(*args) 
kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
myFun2(**kwargs) 

msg = '''
Lamda function
lambda [arg1 [,arg2,.....argn]]:expression
'''
print('\n'*2,msg)
mysum = lambda arg1, arg2: arg1 + arg2
# Now you can call sum as a function
print ("Value of total : ", mysum( 10, 20 ))
print ("Value of total : ", mysum( 20, 20 ))

msg = '''
Scope of Variables
'''
print('\n'*2,msg)

msg = '''
We can access the global variable without using global keyword
But don't assign the variable after accessing it
'''
print('\n'*2,msg)
global_var = 5
def useglobal():
    print('Using global variable without using global keyword:',global_var)
    
useglobal()

msg = '''
But don't assign the variable after accessing it
'''
print('\n'*2,msg)
def useglobal_dont_assign():
    print('Using global variable without using global keyword:',global_var)
    global_var = 10

try:
    useglobal_dont_assign()
except Exception as e:
    print(e)

msg = '''
Before accessing global variable if it is assigned( without using global keyword)
It will become local to function
'''
print('\n'*2,msg)
total = 0   # This is global variable.
# Function definition is here
def mysum2( arg1, arg2 ):
    # Add both the parameters and return them."
    total = arg1 + arg2; # Here total is local variable.
    print ("Inside the function local total : ", total)
    return total

# Now you can call sum function
mysum2( 10, 20 )
print ("Outside the function global total : ", total )

msg = '''
With global keyword after accessing variable we can reassign global Variable
'''
print('\n'*2,msg)
total = 0   # This is global variable.
# Function definition is here
def mysum3( arg1, arg2 ):
    # Add both the parameters and return them."
    global total
    print(total)
    total = arg1 + arg2; # Here total is local variable.
    print ("Inside the function local total : ", total)
    return total

# Now you can call sum function
print ("Before calling the function global total : ", total )
mysum3( 10, 20 )
print ("After calling the function global total : ", total )


'''
Notes
1) All parameters (arguments) in the Python language are passed by reference.

2) foo(*args)        --> f(xyz) means args = (xyz), args will be xyz inside tuple

3) myFun(**kwargs)   --> myFun(first ='Geeks', mid ='for', last='Geeks')
                     --> kwargs= {'first': 'Geeks', 'mid': 'for', 'last': 'Geeks'}
                     
4) myFun2(arg1, arg2, arg3)
                     -->
                        args = ("Geeks", "for", "Geeks") 
                        myFun2(*args) 
                        kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
                        myFun2(**kwargs) 
 
We can access the global variable without using global keyword
But don't reassign the variable after accessing it

Before accessing global variable if it is assigned( without using global keyword)
It will become local to function

With global keyword after accessing variable we can reassign global Variable
'''