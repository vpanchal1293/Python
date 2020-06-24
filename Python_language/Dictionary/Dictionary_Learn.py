msg = '''
Each key is separated from its value by a colon (:),
the items are separated by commas, and the whole thing is enclosed in curly braces.
An empty dictionary without any items is written with just two curly braces, like this: {}.
Keys are unique within a dictionary while values may not be.
The values of a dictionary can be of any type,
but the keys must be of an immutable data type such as strings, numbers, or tuples.
'''
dict_var = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict_var['Name']: ", dict_var['Name'])
print ("dict_var['Age']: ", dict_var['Age'])

print('\n'*2,'Updating Variable')
dict_var['school'] = 'ABC'
print(dict_var)

print('\n'*2,'Deleting dict key')
dict_var = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict_var)
del dict_var['Name'] # remove entry with key 'Name
print(dict_var)

print('\n'*2,'Delete All element')
dict_var = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict_var)
dict_var.clear()     # remove all entries in dict
print(dict_var)

print('\n'*2,'Delete Dict variable')
dict_var = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict_var)
del dict_var         # delete entire dictionary
try:
    print(dict_var)
except Exception as error:
    print(error)
    
print('\n'*2,'Rules of Dict')
rule_1 = '''
More than one entry per key is not allowed.
This means no duplicate key is allowed.
When duplicate keys are encountered during assignment, 
the last assignment wins.
'''
print(rule_1)
dict_var = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print ("dict_var['Name']: ", dict_var['Name'])

rule_2 = '''
Keys must be immutable. This means you can use strings,
numbers or tuples as dictionary keys but something like ['key'] is not allowed
'''
print('\n'*2,rule_2)
try:
    dict_var = {['Name']: 'Zara', 'Age': 7}
except Exception as e:
    print(e)
print(dict_var)

'''
Function & Description
'''
print('\n'*2)
dict_var = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} 
print("len of dict dict_var = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}")
print('len(dict_var) ',len(dict_var))

print('\n'*2)
dict_var = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} 
print("string representation of dict")
print('str(dict_var)',str(dict_var))

print('\n'*2)
dict_var = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} 
print("type(dict_var)",type(dict_var))

'''
Methods
'''
print('\n'*2,'dict_var.clear()','Removes all elements of dictionary dict')
dict_var = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print(dict_var)
print('dict.clear()')
dict_var.clear()
print(dict_var)

print('\n'*2,'dict_var.copy()','Returns a shallow copy of dictionary dict')
print('if dict_var_2 = dict_var_1 will create symbolic link, updating one will update also')
print('But dict_var_2 = dict_var_1.copy() will create new variable and copy items to new place')
dict_var_1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict_var_2 = dict_var_1.copy()
print('dict_var_1',dict_var_1)
print('dict_var_2',dict_var_2)
dict_var_1.clear()
print('dict_var_1',dict_var_1)
print('dict_var_2',dict_var_2)


msg = '''
fromkeys()
creates a new dictionary with keys from seq and values set to value.

Syntax
Following is the syntax for fromkeys() method −

dict.fromkeys(seq[, value]))
Parameters
seq − This is the list of values which would be used for dictionary keys preparation.

value − This is optional, if provided then value would be set to this value

Return Value
This method returns the list.
'''
print('\n'*2,msg)
seq = ('name', 'age', 'sex')

dict_var = dict.fromkeys(seq)
print ("New Dictionary : " ,  str(dict_var))

dict_var = dict.fromkeys(seq, 10)
print ("New Dictionary : " , str(dict_var))


msg = '''
dict_var.get(key, default=None)
key − This is the Key to be searched in the dictionary.
default − This is the Value to be returned in case key does not exist.

Return Value
This method return a value for the given key.
If key is not available, then returns default value None.

'''
print('\n'*2,msg)
dict_var = {'Name': 'Zara', 'Age': 27}

print ("Value : %s" %  dict_var.get('Age'))
print ("Value : %s" %  dict_var.get('Sex', "NA"))

msg = '''
dict_var.items()

Return Value
This method returns a list of tuple pairs(dict_items).
'''
dict_var = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" %  dict_var.items())

msg = '''
dict.keys()
Return Value
This method returns a list of all the available keys in the dictionary((dict_keys).
'''
dict_var = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" %  dict_var.keys())

msg = '''
dict_var.values()
Return Value
This method returns a list of all the available values in the dictionary((dict_values).
'''
dict_var = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" %  dict_var.values())


msg = '''
dict.setdefault(key, default = None)
Parameters
key − This is the key to be searched.
default − This is the Value to be returned in case key is not found.

Return Value
This method returns the key value available in the dictionary
and if given key is not available then it will return provided default value.
'''
print('\n'*2,msg)
dict_var = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" %  dict_var.setdefault('Age', None))
print ("Value : %s" %  dict_var.setdefault('Sex', 'NA'))
print (dict_var)

msg = '''
dict_var_1.update(dict_var_2)
Parameters
dict_var_2 − This is the dictionary to be added into dict_var_1.
'''
print('\n'*2,msg)
dict_var_1 = {'Name': 'Zara', 'Age': 7}
dict_var_2 = {'Sex': 'female' }

dict_var_1.update(dict_var_2)
print ("updated dict : ", dict_var_1)

'''
dict_var = {'Name': 'Zara', 'Age': 7}
dict_var.clear()
dict_var.copy
dict_var.fromkeys
dict_var.get
dict_var.items
dict_var.keys
dict_var.pop
dict_var.popitem
dict_var.setdefault
dict_var.update
dict_var.values
'''

d = {}
a = 5
d[a] = '5'
#print(d) -> {5:'5'}
a = 7
#print(d) -> still {5:'5'}
