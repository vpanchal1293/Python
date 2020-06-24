msg = '''
why generators
However, generators can be better in terms of both memory use and performance in
larger programs. They allow functions to avoid doing all the work up front, which is
especially useful when the result lists are large or when it takes a lot of computation to
produce each value. Generators distribute the time required to produce the series of
values among loop iterations.
'''

print(msg)

msg = '''
A generator-function is defined like a normal function, 
but whenever it needs to generate a value, 
it does so with the yield keyword rather than return. 
If the body of a def contains yield, 
the function automatically becomes a generator function'''
print(msg)
def gensquares(N):
    for i in range(N):
        yield i ** 2

for i in gensquares(5): # Resume the function
    print(i, end=' : ') # Print last yielded value
print('\n')


msg = '''
Calling generator function will return generator object
it will not execute function while calling it
'''
print(msg)
x = gensquares(5)
print(type(x))


msg = '''
next(x) will return next iteration value
When there is no value it will raise StopIteration exception
'''
print(msg)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
try:
    print(next(x))
except Exception as e:
    print("This is StopIteration error")
    print(type(e).__name__,e)

msg = '''
generator_object.close()
Used to Stop the generator

close method that raises a
special GeneratorExit exception inside the generator to terminate the iteration entirely.
'''
print(msg)
x = gensquares(5)
print(next(x))
print(next(x))
x.close()
try:
    print(next(x))
except Exception as e:
    print("generator.close() stops generator so This is StopIteration error ")
    print(type(e).__name__,e)

msg = '''
generator_object.send()
send the value to yield 
-- send will generate next value(next will be called implicitly) 
-- Before starting generator send should not be called
why:
The send method can be used, for example, to code a generator that its caller can terminate
by sending a termination code, or redirect by passing a new position in data
being processed inside the generator
consider following example
'''
print(msg)
def gencubess(N):
    for i in range(N):
        recv_val = (yield i ** 3)
        print('recv_val:',recv_val)

cubes = gencubess(10)
print(type(cubes))
print(next(cubes))
print(next(cubes))
print(next(cubes))
print(cubes.send("1st Message to generator"))
print(next(cubes))
print(cubes.send("2nd Message to generator"))
print(next(cubes))

msg = '''
Generator Expressions
(x*x for x in range(10))

why

generator expressions may also run slightly slower than list comprehensions
in practice, so they are probably best used only for very large result sets,
or applications that cannot wait for full results generation. 
A more authoritative statement about performance,
'''
print(msg)
GE = (x ** 2 for x in range(4))
print(next(GE))
print(next(GE))
print(next(GE))
print(next(GE))
try:
    print(next(GE))
except Exception as e:
    print("This is StopIteration error ")
    print(type(e).__name__,e)

msg = '''
Other way of calling generator Expression
'''
print(msg)
for num in (x ** 2 for x in range(4)): # Calls next() automatically
    print('%s, %s' % (num, num / 2.0))


s = sum(x ** 2 for x in range(4)) # Parens optional
print(s)
soreted_list = sorted(x ** 2 for x in range(4)) # Parens optional
print(soreted_list)
reverse_soreted_list = sorted((x ** 2 for x in range(4)), reverse=True) # Parens required
print(reverse_soreted_list)


msg = '''
Scope of generator variable
y = (x for x in range(5)) 
x is local scope outside we can not access
'''
print(msg)
y = (m for m in range(5)) 
print(y)
try:
    print(m)
except Exception as e:
    print('m is not available outside')
    print(type(e).__name__,e)
    
m = 25
y1 = (m for m in range(5)) 
print(y1)
print("m value is not overwritten for generator:",m)


for m in range(5):
    pass
print("m value is not overwritten for simpel loop:",m)