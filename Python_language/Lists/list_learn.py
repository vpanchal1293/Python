'''
Learn List
'''
print('\n'*2)
list_1 = [1,2,3]
print(list_1)

'''
List Basic operation
'''
print('\n'*2)
print('List Basic operation')
list_1 = [1,2,3]
print("Len", len(list_1))


print('\n'*2)
print('Concatenation')
list_1 = [1,2,3]
list_2 = [4,5,6]
print('list_1 + list_2',list_1+list_2)

print('\n'*2)
print('Repetition')
print('list_1*3',list_1*3)


print('\n'*2)
print('Membership')
print('3 in list_1',3 in list_1)

print('\n'*2)
print('Iteration')
for i in list_1:
    print(i)

print('\n'*2)
list_2 = [4,5,6]
print('Len of list, len(list_1)',len(list_1))

print('\n'*2)
list_1 = [4,5,6]
print('Max of list, max(list_1)',max(list_1))

print('\n'*2)
list_1 = [4,5,6]
print('Min of list, min(list_1)',min(list_1))

print('\n'*2)
str_1 = '1234'
print(list(str_1))

print('\n'*2)
list_1 = [4,5,6,4]
print('Count method list_1.count(4)',list_1.count(4))

print('\n'*2)
list_1 = [4,5,6]
print('append method argument: any object') 
print('argument is appended at end as one element')
print('So size will increase by 1')
list_1.append(7)
print(list_1)
list_1.append([8,9])
print(list_1)


print('\n'*2)
list_1 = [4,5,6]
print('Extend method argument: Iterator')
print('Extended with iterator values')
print('So size will increase length of iterator')
list_1.extend([7,8])
print(list_1)

print('\n'*2)
list_1 = [4,5,6,4]
print('index method, list_1.index(4)',list_1.index(4))
try:
    print('Raise Exception list_1.index(8)',list_1.index(8))
except Exception as msg:
    print(msg)

'''
The insert() method inserts object obj into list at offset index. 
list.insert(index, obj)
Parameters index − This is the Index where the object obj need to be inserted.
obj − This is the Object to be inserted into the given list.
'''
print('\n'*2,'insert()')
list1 = ['physics', 'chemistry', 'maths']
list1.insert(1, 'Biology')
print ('Final list : ', list1)

'''
The pop() method removes and returns last object or obj from the list.
list.pop(obj = list[-1])
Parameters
obj − This is an optional parameter, index of the object to be removed from the list.
Return Value
This method returns the removed object from the list.
'''
print('\n'*2,'pop()')
list1 = ['physics', 'Biology', 'chemistry', 'maths']
print(list1)
list1.pop()
print ("list now : ", list1)
list1.pop(1)
print ("list now : ", list1)


msg = '''>>> a = [0, 2, 3, 2]
>>> a.remove(2) --> remove take item of the list
>>> a
[0, 3, 2]

del removes the item at a specific index:
>>> a = [3, 2, 2, 1]
>>> del a[1]
>>> a
[3, 2, 1]
and pop removes the item at a specific index and returns it.

>>> a = [4, 3, 5]
>>> a.pop(1)
3
>>> a
[4, 5]
'''
print('\n'*2,'Difference between remove del and pop')
print(msg)

'''
The reverse() method reverses objects of list in place.

list.reverse()
This method does not return any value but reverse the given object from the list.
'''
print('\n'*2)
list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.reverse()
print ("list now : ", list1)

'''
The sort() method sorts objects of list, use compare function if given.
list.sort([func])
This method does not return any value; it simply sorts the contents of the given list.
'''
print('\n'*2,'list.sort([func])')
list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.sort()
print ("list now : ", list1)

'''
list comprehension
'''
msg = '''
for x in sequence:
    f(x)

l = [f(x) for x in sequence] 

for x in [1,2,3]:
    l.append(x*x)

l = [x*x for x in [1,2,3]] 

for x in sequence:
    if condition:
        f(x)
[f(x) for x in sequence if condition]

for i in [1,2,3]:
    if i%2 == 0
        l.append('even')

l = ['even' for i in [1,2,3] if i%2 == 0]

for x in sequence:
    if condition:
        f(x)
    else:
        g(x)
[f(x) if condition else g(x) for x in sequence]

for i in [1,2,3]:
    if i%2 == 0:
        l.append('even')
    else:
        l.append('odd')
        
l = ['even' if i%2 == 0 else 'odd'  for i in [1,2,3]]


for sub_sequence in main_sequence:
    for item in sub_sequence:
        f(item)

l = [f(item) for sub_sequence in main_sequence for item in sub_sequence]

for x in [[1,2,3],[4,5,6]]:
    for i in x:
        l.append(i)

l = [ i for x in [[1,2,3],[4,5,6]] for i in x ]

for sub_sequence in main_sequence:
    for item in sub_sequence:
        if condition:
            f(item)

[f(item) for sub_sequence in main_sequence for item in sub_sequence if condition ]

for x in [[1,2,3],[4,5,6]]:
    for i in x:
        if i%2 == 0:
            l.append('even')
        
l = ['even' for x in [[1,2,3],[4,5,6]] for i in x if i%2 == 0 ]


for sub_sequence in main_sequence:
    for item in sub_sequence:
        if condition:
            f(item)
        else:
            g(item)

[f(item) if condition else g(item) for sub_sequence in main_sequence for item in sub_sequence]

for x in [[1,2,3],[4,5,6]]:
    for i in x:
        if i%2 == 0:
            l.append('even')
        else:
            l.append('odd')
        
l = ['even' if i%2 == 0 else 'odd'  for x in [[1,2,3],[4,5,6]] for i in x ]

for sub_sequence in main_sequence:
    if condition:
        for item in sub_sequence:
            f(item)

for i in range(10):
    if (i%2 == 0):
        for j in range(i):
            l.append(j)
            
l = [ j for i in range(10) if (i%2 == 0) for j in range(i)]


'''

'''
list1.append(object)
list1.clear()
list1.copy()
list1.count(value)
list1.extend(iterable)
list1.index(value, start, stop)
list1.insert(index, object)
list1.pop(index)
list1.remove(value)
list1.reverse()
list1.sort(key=None, reverse=False)
'''