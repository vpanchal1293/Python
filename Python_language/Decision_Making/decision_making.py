'''
If
'''
var1 = 100
if var1:
    print ("1 - Got a true expression value",var1)

var2 = 0
if var2:
    print ("2 - Got a true expression value",var2)
    
'''
ternary operator 
x = (value if true) if (expression) else (value if false)
x = (expression) and (value if true) or (value if false)
x = ( (value if false) , (value if true) ) [expression]
x = {True: value if true, False: value if false} [expression]
x = (lambda: value if false, lambda: value if true)[expression]()
'''
v = 4
x = 5 if(v == 3) else 6
print('if v is 3',x)

v = 3
x = 5 if(v == 3) else 6
print(x)


a = 3
b = 2
min = a < b and a or b 
print('min',min) 

print('a and b same' if(a == b) else ('a>b') if (a>b) else ('b>a'))

print( (b, a) [a > b] ) 
print({True: a, False: b} [a > b])

print((lambda: b, lambda: a)[a < b]()) 

'''
value of and and or operation
'''
a = 10
b = 20
c = 30
'''
in and operator both operand will checked.
Answer will be left side operand
a and b -> 20 
20 and 30 -> 30
'''
print(a and b and c) # answer 30

'''
For or operator if first operator is nonzero answer will first operand, here second operand won't be checked
if if first operator is zero second operator nonzero answer will be second operator
if both oerator zero answer will be zero
here below example and has higher priority
10 or 0 or 30
10 or 30 -> (first operand is nonzero answer first operand)
'''
a = 10
b = 0
c = 30
print(a or b and c) 

a = 10
b = 20
c = 30
'''
10 or 20 and 30
10 or 30 
10
'''
print(a or b and c) # answer 10

a = 0
b = 20
c = 30
'''
0 or 20 and 30
0 or 30
30
'''
print(a or b and c) # answer is 30
