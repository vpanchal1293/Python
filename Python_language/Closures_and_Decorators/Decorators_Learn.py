msg = '''
Decorators are very powerful and useful tool in Python
it allows programmers to modify the behavior of function or class.
Decorators allow us to wrap another function 
in order to extend the behavior of wrapped function, without permanently modifying it.

meaning of decorator

@decorator
def foo(a):
    return a
    
meaning of above syntex
foo = decorator(foo)
'''
print('\n'*2,msg)
def decorator_fun(func):
    def wrapper_decorator_fun(*var,**kwarg):
        print('Before function call decoration')
        ret_val = func(*var,**kwarg)
        print('After function call decoration')
        return ret_val
    return wrapper_decorator_fun

@decorator_fun
def add(a,b):
    return a+b

print(add)
ret = add(4,5)
print(ret)

msg = '''
real world ExampleService
Timer
'''
print('\n'*2,msg)
import time
def timer_decorator(func):
    def wrapper_timer_decorator(*var,**kwarg):
        start_time = time.time()
        ret_val = func(*var,**kwarg)
        end_time = time.time()
        time_taken = end_time - start_time
        print('Time taken for function %s is %f seconds' %(func.__name__,time_taken))
        return ret_val
    return wrapper_timer_decorator

@timer_decorator
def cpu_time_cal(n):
    sum = 0
    for i in range(n):
        sum = sum + i

cpu_time_cal(10000000)

msg = '''
debigging function
'''
print('\n'*2,msg)
def debug(func):
    """Print the function signature and return value"""
    
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  
        signature = ", ".join(args_repr + kwargs_repr)           
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           
        return value
    return wrapper_debug

@debug
def sub(a,b):
    return a-b
sub(3,2)


msg = '''
Registering function attributes 
'''
print('\n'*2,msg)
PLUGINS = dict()

def register(func):
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

print(PLUGINS)

msg ='''
Nested decoratord

@decorator_1
@decorator_2
def foo():
    ...
    
meaning
foo = decorator_1(decorator_2(foo)
'''
print('\n'*2,msg)
def decorator_1(func):
    def wrapper_decorator_1(*var,**kwarg):
        print('This is decorator_1')
        return func(*var,**kwarg)
    return wrapper_decorator_1

def decorator_2(func):
    def wrapper_decorator_2(*var,**kwarg):
        print('This is decorator_2')
        return func(*var,**kwarg)
    return wrapper_decorator_2

@decorator_1
@decorator_2
def multi_decoration(a):
    print('This is demo for multi decoration')
    return a

multi_decoration(1)


msg = '''
Decorators With Arguments

@decorator_func_arg(a=10)
def foo():
    ...

foo = (decorator_func_arg(10))(foo)
    --> Because decorator_func_arg(10) returns decorator_func_1
    = decorator_func_1(foo)
'''
print('\n'*2,msg)
def decorator_func_arg(a):
    a_dec = a
    def decorator_func_1(func):
        def wrapper_decorator_func_1(*var,**kwarg):
            nonlocal a_dec
            print('Before function execution')
            print(a_dec)
            a_dec += 1
            ret_val = func(*var,**kwarg)
            print('After function execution')
            return ret_val
        return wrapper_decorator_func_1
    return decorator_func_1

@decorator_func_arg(1)
def mul(a,b):
    return a*b

ret = mul(2,3)
print(ret)


msg = '''
decorator with and without arg
'''
print('\n'*2,msg)
def decorator_func_arg_2(_func = None, a=None):
    aa = a
    def decorator_func_2(func):
        nonlocal aa
        def wrapper_decorator_func_2(*var,**kwarg):
            nonlocal aa
            if aa is not None:
                print('Decorator Arguments : ',aa)
            print('Before function execution')
            ret_val = func(*var,**kwarg)
            print('After function execution')
            return ret_val
        return wrapper_decorator_func_2
    
    if _func is None:
        return decorator_func_2
    else:
        return decorator_func_2(_func)

@decorator_func_arg_2
def mul_2(a,b):
    return a*b

mul_2(2,3)

msg = '''
Here without argument decorator call will be

foo = decorator(foo)

mul_2 = decorator_func_arg_2(mul_2)
        -> _func = mul_2 (not none)
mul_2 = decorator_func_2(mul_2)
'''
print('\n'*2,msg)
@decorator_func_arg_2(a = 4)
def mul_3(a,b):
    return a*b

msg = '''
Here decorator with argument means

mul_3 = (decorator_func_arg_2( a=4 )) (mul_3)
      = (decorator_func_arg_2(_func = None, a=4 )) (mul_3)
        -> _func = None so return value is decorator_func_2
        -> so (decorator_func_arg_2(_func = None, a=4 ))  returns decorator_func_2
mul_3 = decorator_func_2(mul_3)
'''
print('\n'*2,msg)
mul_3(4,5)


mag = '''
Stateful decorators 
Using function State
'''

def state_decorator(func):
    def wrapper_state_decorator(*vars, **kwargs):
        print("Before decorator")
        print('State: ',wrapper_state_decorator.state)
        ret = func(*vars, **kwargs)
        wrapper_state_decorator.state += 1 
        print('After decorator')
        return ret
    wrapper_state_decorator.state = 0
    return wrapper_state_decorator

@state_decorator
def mul_4(a,b):
    return a*b

mul_4(1,2)
mul_4(4,3)
mul_4(5,6)
print('state after all calls:',mul_4.state)