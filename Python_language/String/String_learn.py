'''
Learn String
'''
var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

'''
item assignemtn is not possible in python
'''
print('\n'*2)
print('Assignment in string')
try:
    var1 = 'Hello World!'
    var1[1] = 'b'
except Exception as e:
    print(e) 

'''
Updating Strings
You can "update" an existing string by (re)assigning a variable to another string. 
The new value can be related to its previous value or to a completely different string altogether.
'''
print('\n'*2)
var1 = 'Hello World!'
print('old var1 id: ',id(var1))
var1 = var1[:6] + 'Python'
print ("Updated String :- ", var1)
print('old var1 id: ',id(var1))

