msg = '''
Simple closure
'''
print('\n'*2,msg)
def muitiplier(N):
    def inner(i):
        return i * N
    return inner

mul_5 = muitiplier(5)
print(mul_5)
print(mul_5(2))
print(mul_5(3))

mul_2 = muitiplier(2)
print(mul_2)
print(mul_2(2))
print(mul_2(3))

def adder(N):
    return lambda i : i + N

add_2 = adder(2)
print(add_2)
print(add_2(1))
print(add_2(2))
print(add_2(3))      

msg = '''
from test.test_warnings.data.stacklevel import inner
from unittest.test.testmock.testpatch import function
from _ast import keyword
here inner function can read the value of outside functions's variable
But if same variable is assigned a value then it will generate error 
'''
print('\n'*2,msg)
def out_fun_1(N):
    n = N
    def in_fun_1(i):
        print('New reference of i is created as n')
        n = i       # But here assigned, Not read so new reference will created for i an n
        return n
    return in_fun_1

c1 = out_fun_1(5)
print(c1(2))

def out_fun_2(N):
    n = N
    def in_fun_2(i):
        print('Outside n read:',n)      # Here just used so it will use outside n
        return n                        # Here it is just used not modified
    return in_fun_2

c2 = out_fun_2(5)
print(c2(2))

print(msg)
def out_fun_3(N):
    n = N
    def in_fun_3(i):
        print('Here it can read value, Due to below statement it will give error')
        print(n)        #Here it can read value, Due to below statement it will give error
        print('But here it is read and assigned so it will search for definition')
        n = n + i       # But here it is read and assigned so it will search for definition
        return n
    return in_fun_3

c3 = out_fun_3(5)
try:
    c3(2)
except Exception as e:
    print(type(e).__name__,e)


def out_func_4():
    list_var_out = []
    def in_fun_4(i):
        print("Here only read not modified")
        print("list_var_out before append:",list_var_out)
        list_var_out.append(i)      #this is kind of read only
        return list_var_out
    return in_fun_4

slicer_4 = out_func_4()
print(slicer_4)
print(slicer_4(1))
print(slicer_4(2))
print(slicer_4(3))

def out_func_5():
    list_var_out = []
    def inner(i):
        print("new list_var_out is created:")
        list_var_out = [i]
        return list_var_out
    return inner

maker = out_func_5()
print(maker)
print(maker(1))
print(maker(2))

def out_func_6():
    list_var_out = []
    def inner(i):
        print("Here list_var_out is used and assigned new reference:")
        list_var_out = list_var_out + [i]
        return list_var_out
    return inner

maker_2 = out_func_6()
print(maker_2)
try:
    print(maker_2(1))
except Exception as e:
    print(type(e).__name__,e)

msg = '''
Non local keyword to use variable of out_fun inside inner function
'''
print('\n'*2,msg)
def out_fun_7(N):
    n = N
    def in_fun_3(i):
        nonlocal n
        print('it can access means read and update variable n due to nonlocal keyword')
        print(n)
        n = n + i
        return n
    return in_fun_3

c7 = out_fun_7(8)
print(c7)
print(c7(1))
print(c7(1))
print(c7(1))
print(c7(1))


def out_func_8():
    list_var_out = []
    def inner(i):
        nonlocal list_var_out
        print("Here we can access list_var_out due to nonlocal keyword:")
        list_var_out = list_var_out + [i]
        return list_var_out
    return inner

maker_3 = out_func_8()
print(maker_3)
print(maker_3(1))
print(maker_3(2))
print(maker_3(3))


msg = '''
Some facts for nonlocal keyword

if variable is not defined in out_fun and it is defined 
nonlocal in inner function it will raise exception
while defining function it will generate error
def out_fun_9():
    def inner():
        nonlocal m -->SyntaxError: no binding for nonlocal 'm' found
    return inner


m = 10
def out_fun_9():
    def inner():
        nonlocal m -->SyntaxError: no binding for nonlocal 'm' found
    return inner

global -->
makes scope lookup begin in the enclosing module's scope and allows
names there to be assigned. Scope lookup continues on to the built-in scope if the
name does not exist in the module, but assignments to global names always create
or change them in the module's scope.

nonlocal -->
restricts scope lookup to just enclosing defs, requires that the names already
exist there, and allows them to be assigned. Scope lookup does not continue
on to the global or built-in scopes.
'''
print('\n'*2,msg)
def tester(start):
    global state # Move it out to the module to change it
    state = start # global allows changes in module scope
    def nested(label):
        global state
        print(label, state)
        state += 1
    return nested

F = tester(0)
F('Hello')
F('HI')

G = tester(34)
G('How')
G('are')

F("Hey")

msg = '''
Here due to only one state keyword
it is same for all function object created separately 
If we want to give separate one option is nonlocal
other option is function attribute
'''
print('\n'*2,msg)
def tester_2(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested

F1 = tester_2(0)
G1 = tester_2(34)

F1('Hello')
F1('HI')
G1('How')
G1('are')
F1("Hey")

def tester_3(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested

F3 = tester_3(0)
G3 = tester_3(34)
F3('Hello')
F3('HI')
G3('How')
G3('are')
F3("Hey")
F3('vipul')

msg = '''
small example on function attribute
'''
print('\n'*2,msg)
def fn(i):
    fn.f += i
    return fn.f
fn.f = 1


