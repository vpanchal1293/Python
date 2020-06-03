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