'''
numbers
int
float
real
'''

int_type = 5
print(type(int_type))

float_type = 10.5
print(type(float_type))

complex_type = 1 + 2j
print(type(complex_type))

'''
type conversion
'''
'''string to int'''
print('\n'*2)
print('string to int')
st = '0'
print(int(st))

'''float to int'''
print('\n'*2)
print('float to int')
flt = 1.6
print(int(flt))

'''string to float'''
print('\n'*2)
print('string to float')
st = '1.5'
print(float(st))

'''int to float'''
print('\n'*2)
print('int to float')
it = 1
print(float(it))

'''
complex
'''
print('\n'*2)
print('complex(real)')
real = 1
img = 3
print(complex(real))

print('complex(real)')
print(complex(real,img))
print('\n'*2)

'''
1    abs(x)
The absolute value of x: the (positive) distance between x and zero.

2    ceil(x)
The ceiling of x: the smallest integer not less than x.

3    
cmp(x, y)

-1 if x < y, 0 if x == y, or 1 if x > y. Deprecated in Python 3. Instead use return (x>y)-(x<y).

4    exp(x)
The exponential of x: ex

5    fabs(x)
The absolute value of x.

6    floor(x)
The floor of x: the largest integer not greater than x.

7    log(x)
The natural logarithm of x, for x > 0.

8    log10(x)
The base-10 logarithm of x for x > 0.

9    max(x1, x2,...)
The largest of its arguments: the value closest to positive infinity

10    min(x1, x2,...)
The smallest of its arguments: the value closest to negative infinity.

11    modf(x)
The fractional and integer parts of x in a two-item tuple. Both parts have the same sign as x. The integer part is returned as a float.

12    pow(x, y)
The value of x**y.

13    round(x [,n])
x rounded to n digits from the decimal point. Python rounds away from zero as a tie-breaker: round(0.5) is 1.0 and round(-0.5) is -1.0.

14    sqrt(x)
The square root of x for x > 0.

'''

'''abs'''

print('\n'*2)
print('abs')
print ("abs(-45) : ", abs(-45))
print ("abs(100.12) : ", abs(100.12))
print ("abs(-55.45) : ", abs(-55.45))


import math
'''
math.ceil( x )
x   This is a numeric expression.
The ceil() method returns the ceiling value of x i.e. the smallest integer greater than than x.
'''
print('\n'*2)
print ("math.ceil(-45.17) : ", math.ceil(-45.17))
print ("math.ceil(100.12) : ", math.ceil(100.12))
print ("math.ceil(100.72) : ", math.ceil(100.72))
print ("math.ceil(math.pi) : ", math.ceil(math.pi))

'''
math.exp( x )
x   This is a numeric expression.
This method returns exponential of x: ex
'''
print('\n'*2)
print ("math.exp(-45.17) : ", math.exp(-45.17))
print ("math.exp(100.12) : ", math.exp(100.12))
print ("math.exp(100.72) : ", math.exp(100.72))
print ("math.exp(math.pi) : ", math.exp(math.pi))

'''
abs() is a built in function whereas fabs() is defined in math module.
fabs() function works only on float and integer whereas abs() works with complex number also.
'''
print('\n'*2)
print ("math.fabs(-45.17) : ", math.fabs(-45.17))
print ("math.fabs(100.12) : ", math.fabs(100.12))
print ("math.fabs(100.72) : ", math.fabs(100.72))
print ("math.fabs(math.pi) : ", math.fabs(math.pi))


'''
The floor() method returns the floor of x i.e. the largest integer not greater than x.
math.floor(x)
x   This is a numeric expression.
This method returns the largest integer not greater than x.
'''
print('\n'*2)
print ("math.floor(-45.17) : ", math.floor(-45.17))
print ("math.floor(100.12) : ", math.floor(100.12))
print ("math.floor(100.72) : ", math.floor(100.72))
print ("math.floor(math.pi) : ", math.floor(math.pi))


'''
The log() method returns the natural logarithm of x, for x > 0.
math.log( x )
Parameters : x ’ This is a numeric expression.
Return Value : This method returns natural logarithm of x, for x > 0.
'''
print('\n'*2)
print ("math.log(100.12) : ", math.log(100.12))
print ("math.log(100.72) : ", math.log(100.72))
print ("math.log(math.pi) : ", math.log(math.pi))

'''
The log10() method returns base-10 logarithm of x for x > 0.
math.log10( x )
Parameters : x   This is a numeric expression.
Return Value : This method returns natural logarithm of x, for x > 0.
'''
print('\n'*2)
print ("math.log10(100.12) : ", math.log10(100.12))
print ("math.log10(100.72) : ", math.log10(100.72))
print ("math.log10(119) : ", math.log10(119))
print ("math.log10(math.pi) : ", math.log10(math.pi))

'''
This method returns the largest of its arguments.
max(x,y,z,...)
Parameters : all args are numeric expression.
'''
print ("max(80, 100, 1000) : ", max(80, 100, 1000))
print ("max(-20, 100, 400) : ", max(-20, 100, 400))
print ("max(-80, -20, -10) : ", max(-80, -20, -10))
print ("max(0, 100, -400) : ", max(0, 100, -400))

'''
This method returns the largest of its arguments.
min(x,y,z,...)
Parameters : all args are numeric expression.
'''
print ("min(80, 100, 1000) : ", min(80, 100, 1000))
print ("min(-20, 100, 400) : ", min(-20, 100, 400))
print ("min(-80, -20, -10) : ", min(-80, -20, -10))
print ("min(0, 100, -400) : ", min(0, 100, -400))

'''
The modf() method returns the fractional and integer parts of x in a two-item tuple. 
Both parts have the same sign as x. The integer part is returned as a float.
math.modf( x )
x   This is a numeric expression.
'''
print('\n'*2)
print ("math.modf(100.12) : ", math.modf(-100.12))
print ("math.modf(100.72) : ", math.modf(100.72))
print ("math.modf(119) : ", math.modf(119))
print ("math.modf(math.pi) : ", math.modf(math.pi))

'''
pow(x,y)
This method returns the value of x^y.
x,y   This is a numeric expression.
'''
print('\n'*2)
print ("math.pow(100, 2) : ", math.pow(100, 2))
print ("math.pow(100, -2) : ", math.pow(100, -2))
print ("math.pow(2, 4) : ", math.pow(2, 4))
print ("math.pow(3, 0) : ", math.pow(3, 0))

'''
round( x [, n]  )
is a built-in function in Python. 
It returns x rounded to n digits from the decimal point.
x   This is a numeric expression.
n   Represents number of digits from decimal point up to which x is to be rounded. Default is 0.
'''
print('\n'*2)
print ("round(70.23456) : ", round(70.23456))
print ("round(56.659,1) : ", round(56.659,1))
print ("round(80.264, 2) : ", round(80.264, 2))
print ("round(100.000056, 3) : ", round(100.000056, 3))
print ("round(-100.000056, 3) : ", round(-100.000056, 3))

'''
math.sqrt( x )
x   This is a numeric expression.
'''
print('\n'*2)
print ("math.sqrt(100) : ", math.sqrt(100))
print ("math.sqrt(7) : ", math.sqrt(7))
print ("math.sqrt(math.pi) : ", math.sqrt(math.pi))