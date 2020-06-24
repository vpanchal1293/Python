import time
msg = '''
Using default arguments decorators
Slowing down function execution
'''
print('\n'*2,msg)
def slow_decorator(_func = None, delay = None):
    def delay_decorator(func):
        def wrapper_delay_decorator(*var,**kwargs):
            print('Before execution')
            print('delay:',delay)
            if delay is not None:
                time.sleep(delay)
            ret_val = func(*var,**kwargs)
            print('After execution')
            return ret_val
        return wrapper_delay_decorator
    if _func is None:
        return delay_decorator
    else:
        return delay_decorator(_func)

@slow_decorator
def mul(a,b):
    return a*b

@slow_decorator(delay = 2)
def mul_2(a,b):
    return a*b

mul(1,2)
mul_2(1,2)
from unittest.test.testmock.testpatch import function


msg = '''
Creating Singletons
using decorator function state 
'''
print('\n'*2,msg)
def singletons_decorator(cls):
    def wrapper_singletons_decorator(*var,**kwarg):
        if not wrapper_singletons_decorator.instance:
            wrapper_singletons_decorator.instance = cls(*var,**kwarg)
        return wrapper_singletons_decorator.instance
    wrapper_singletons_decorator.instance = None
    return wrapper_singletons_decorator

@singletons_decorator
class abc():
    pass

a1 = abc()
print(id(a1))
a2 = abc()
print(id(a1))
print(a1 is a2)

msg = '''
Caching Return Values
using decorator function state
'''
print('\n'*2,msg)
def ret_val_save_decorator(func):
    def wrapper_ret_val_save_decorator(*var,**kwarg):
            cache_key = var + tuple(kwarg.items())
            ret = func(*var,**kwarg)
            wrapper_ret_val_save_decorator.catch[cache_key] = ret
            return ret
    wrapper_ret_val_save_decorator.catch = {}
    return wrapper_ret_val_save_decorator

@ret_val_save_decorator
def mul_3(a,b):
    return a*b

mul_3(1,2)
mul_3(3,4)
mul_3(5,6)
print('mul_3 trace',mul_3.catch)

msg = '''
for adding new attribute to function
Using default arguments decorators

def decorator(val):
    def wrapper_decorator(func):
        func.name = val
        return func
    return wrapper_decorator

@decorator('abc')
def foo:
    ...
    
meaning
foo = (decorator('abc'))(foo)
foo = func --> here function is foo but with attribute with foo.name = val
'''
print('\n'*2,msg)
def add_attributer_decorator(attribute_val):
    def wrapper_add_attributer_decorator(func):
        print('attribute :',attribute_val)
        func.attribute_name = attribute_val
        return func 
    return wrapper_add_attributer_decorator

@add_attributer_decorator('multiply')
def mul_4(a,b):
    return a*b

print(mul_4.attribute_name)