


import random

'''
1    choice(seq)
A random item from a list, tuple, or string.

2    randrange ([start,] stop [,step])
A randomly selected element from range(start, stop, step).

3    random()
A random float r, such that 0 is less than or equal to r and r is less than 1

4    seed([x])
Sets the integer starting value used in generating random numbers. Call this function before calling any other random module function. Returns None.

5    shuffle(lst)
Randomizes the items of a list in place. Returns None.

6    uniform(x, y)
A random float r, such that x is less than or equal to r and r is less than y.
'''



'''
choice( seq )
The choice() method returns a random item from a list, tuple, or string.
seq − This could be a list, tuple, or string.
'''
print('\n'*2)
print ("returns a random number from range(100) : ",random.choice(range(100)))
print ("returns random element from list [1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
print ("returns random character from string 'Hello World' : ", random.choice('Hello World'))

'''
The randrange() method returns a randomly selected element from range(start, stop, step).

randrange ([start,] stop [,step])
start − Start point of the range. This would be included in the range. Default is 0
stop − Stop point of the range. This would be included in the range. Default is 1
step − Step point of the range. This would be excluded from the range.
'''
print('\n'*2)
# randomly select an odd number between 1-100 
print ("randrange(1,100, 2) : ", random.randrange(1, 100, 2))
# randomly select a number between 0-99 
print ("randrange(100) : ", random.randrange(100))

'''
The random() method returns a random floating point number in the range [0.0, 1.0].
random ( )
Note − This function is not accessible directly, so we need to import the random module and then we need to call this function using the random static object.
Return Value This method returns a random float r, such that 0.0 <= r <= 1.0
'''
print('\n'*2)
# First random number
print ("random() : ", random.random())
# Second random number
print ("random() : ", random.random())


'''
The seed() method initializes the basic random number generator. Call this function before calling any other random module function.
Syntax
seed ([x], [y])
Parameters
x − This is the seed for the next random number. 
If omitted, then it takes system time to generate the next random number. 
If x is an int, it is used directly.

y − This is version number (default is 2).
str, byte or byte array object gets converted in int. Version 1 used hash() of x.

Return Value
This method does not return any value.
'''
print('\n'*2)
random.seed()
print ("random number with default seed", random.random())
random.seed(10)
print ("random number with int seed", random.random())
random.seed("hello",2)
print ("random number with string seed", random.random())

'''
The shuffle() method randomizes the items of a list in place.
shuffle (lst,[random])
Parameters
lst − This could be a list or tuple.
random − This is an optional 0 argument function returning float between 0.0 - 1.0. Default is None
'''
print('\n'*2)
ll = [20, 16, 10, 5];
random.shuffle(ll)
print ("Reshuffled list : ",  ll)
random.shuffle(ll)
print ("Reshuffled list : ",  ll)

'''
Description
The uniform() method returns a random float r
,such that x is less than or equal to r and r is less than y.
uniform(x, y)
Parameters
x − Sets the lower limit of the random float.
y − Sets the upper limit of the random float.
'''
print('\n'*2)
print ("Random Float uniform(5, 10) : ",  random.uniform(5, 10))
print ("Random Float uniform(7, 14) : ",  random.uniform(7, 14))
