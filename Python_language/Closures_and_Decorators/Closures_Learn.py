msg = '''
A Closure is a function object that remembers values in enclosing scopes 
even if they are not present in memory.

1) It is a record that stores a function together with an environment: 
a mapping associating each free variable of the function 
(variables that are used locally, but defined in an enclosing scope) 
with the value or reference to which the 
name was bound when the closure was created.

2 ) A closure - unlike a plain function-allows the function 
to access those captured variables through the closure's
copies of their values or references, even when 
the function is invoked outside their scope.
'''
print('\n'*2,msg)
def print_msg(msg):
    def printer():
        print(msg)
    return printer  
another = print_msg("Hello")
another()
'''
The print_msg() function was called with the string 
"Hello" and the returned function was bound to the name another. 
On calling another(), the message was still remembered although 
we had already finished executing the print_msg() function.

This technique by which some data 
("Hello in this case) gets attached to the code 
is called closure in Python.

This value in the enclosing scope is remembered even when the 
variable goes out of scope or the function itself is removed from the current namespace.
'''
print('\n'*2,msg)
del print_msg
another()
try:
    print_msg
except Exception as e:
    print(type(e).__name__,e)
    
msg = '''
When to use closures?
So what are closures good for?

Closures can avoid the use of global values and provides some form of data hiding. 
It can also provide an object oriented solution to the problem.

When there are few methods (one method in most cases) 
to be implemented in a class, closures can provide 
an alternate and more elegant solution.
But when the number of attributes and methods get larger, 
it's better to implement a class.

Python Decorators make an extensive use of closures as well
'''
print('\n'*2,msg)
def print_msg_2():
    var_1 = 'Hello'
    var_2 = 2
    var_3 = [1,2,3]
    def printer():
        print("Inside inner Function")
        print(var_1,var_2,var_3)
    return printer  
another_2 = print_msg_2()
print(another_2)
another_2()
print(another_2.__closure__[0].cell_contents)

for v in another_2.__closure__:
    print(v.cell_contents)