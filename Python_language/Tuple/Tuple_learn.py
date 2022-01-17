msg = '''
A tuple is a sequence of Python objects
Tuples are sequences, just like lists.
The main difference between the tuples and the lists is that the tuples cannot be changed unlike lists.
Tuples use parentheses, whereas lists use square brackets.
Lists are mutable	Tuples are immutable
List iterations is Time-consuming  Tuple iterations is comparatively Faster than List
List has many function(insertion,deletion) Tuple data type is appropriate for accessing the elements
Lists consume more memory	Tuple consume less memory compared to list
'''
print(msg)

tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
tup4 = (50,)
print(tup4)

print('\n'*2)
print ("Deleting tuple")
print (tup1)
del tup1
print ("After deleting tup : ")
try:
    print (tup1)
except Exception as error:
    print(error)
    
'''
tuple Basic operation
'''
print('\n'*2)
print('tuple Basic operation')
tup_1 = (1,2,3)
print("Len", len(tup_1))


print('\n'*2)
print('Concatenation')
tup_1 = (1,2,3)
tup_2 = (4,5,6)
print('tup_1 + tup_2',tup_1+tup_2)

print('\n'*2)
print('Repetition')
print('tup_1*3',tup_1*3)


print('\n'*2)
print('Membership')
print('3 in tup_1',3 in tup_1)

print('\n'*2)
print('Iteration')
for i in tup_1:
    print(i)

print('\n'*2)
tup_2 = (4,5,6)
print('Len of tup, len(tup_1)',len(tup_1))

print('\n'*2)
tup_1 = (4,5,6)
print('Max of tup, max(tup_1)',max(tup_1))

print('\n'*2)
tup_1 = (4,5,6)
print('Min of tup, min(tup_1)',min(tup_1))

print('\n'*2)
str_1 = '1234'
print(tuple(str_1))

msg = '''
Tuple is immutable but items in are tuple can be mutable and we can change it'''
print('\n'*2)
print(msg)
tup_1 = ([1,2,3],4)
tup_1[0][1] = 5
print(tup_1)

msg = '''
adding only one item in tuple'''
tup_1 = ([1,2,3])
print(tup_1)
tup_1 = ([1,2,3],)
print(tup_1)
