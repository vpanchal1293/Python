
msg = '''
A Set is an unordered collection data type that is iterable, 
mutable and has no duplicate elements
This is based on a data structure known as a hash table. Since sets are unordered, 
we cannot access items using indexes like we do in lists

Sets are unordered.
Set elements are unique. Duplicate elements are not allowed.
A set itself may be modified, 
but the elements contained in the set must be of an immutable type

x = set(iterable object)

empty set creation
empty_set = set()
'''
print(msg,end = '\n\n')

print("Creating set")
set_1 = {1,2,3,4,5}
print(set_1,end = '\n\n')

print("Creating set using set(iterable object)")
set_2 = set([4,5,6])
print(set_2,end = '\n\n')

print("Creating set using string")
set_3 = set("google")
print(set_3,end = '\n\n')

print("Frozen set can;t be change after creation")
frozen_set_1 = frozenset([7,8,9])
print(frozen_set_1,end = '\n\n')

print("Creating empty set")
empty_set = set()
print(empty_set,end = '\n\n')

print("If same elemet in iterable object")
same_elemet_set = {1,1,1,1}
print(same_elemet_set,end = '\n\n')

print("Any set element can't be mutable object")
try:
    non_hasable_invalid_set = {[1,2,3]}
except Exception as e:
    print(e,end = '\n\n') 
tupple_as_element = {(1,2,3),4}
print(tupple_as_element)

msg = '''
add
set_elemet.add()
arg = single immutable object
If you add same element present in set
If won't update anything and won't give error
'''
print(msg)
set_1 = {1,2,3}
set_1.add(4)
print(set_1)
set_1.add(1)
print(set_1)

msg = '''
remove
set_elemet.remove()
arg = element present in set
if given arg is not element of set generate error
'''
print(msg)
set_1 = {1,2,3}
set_1.remove(1)
print(set_1)
try:
    set_1.remove(7)
except Exception as e:
    print("This is exception for remove")
    print(type(e).__name__,e)
    
msg = '''
discard
set_elemet.discard()
arg = element present in set
if given arg is not element of set i won't generate error
'''
print(msg)
set_1 = {1,2,3}
set_1.discard(1)
print(set_1)
set_1.discard(7)
print(set_1)


msg = '''
pop
set_elemet.pop()
return val = remove random element form set and returns 
for empty set generates error
'''
print(msg)
set_1 = {1,2,3}
pop_item = set_1.pop()
print(set_1)
print(pop_item)
empty_set = set()
try:
    empty_set.pop()
except Exception as e:
    print("This is exception for pop for empty set")
    print(type(e).__name__,e)
    

msg = '''
clear
set_elemet.clear()
for empty set generates it won't generate error
'''
print(msg)
set_1 = {1,2,3}
set_1.clear()
print(set_1)
empty_set = set()
empty_set.clear()
print(empty_set)


msg = '''
set of set is not possible
because set is mutable object
set of frozensets are possible
'''
print(msg)
set_1 = frozenset([1,2,3])
set_2 = frozenset([4,5,6])
set_3 = frozenset([7,8,9])
set_of_fset = {set_1,set_2,set_3}
print(set_of_fset)
set_1 = set([1,2,3])
set_2 = set([4,5,6])
set_3 = set([7,8,9])
try:
    set_of_fset = {set_1,set_2,set_3}
except Exception as e:
    print("This is error for set of set")
    print(type(e).__name__,e)


msg = '''
Union of sets
two methods '|' and union
'''
print(msg)
print("Method 1 using '|' operator")
s1 = {1,2,3,4}
s2 = {1,5,6}
s1_u_s2 = s1 | s2
print(s1_u_s2)
print("Method 1 using union function")
s1_un_s2 = s1.union(s2)
print(s1_un_s2)
print("Unnion for more than 2 sets")
s1 = {1,2,3,4}
s2 = {1,5,6}
s3 = {7,8}
s4 = {1,9}
s1_u_s2__u_s3__u_s4 = s1 | s2 | s3 | s4
print(s1_u_s2__u_s3__u_s4)
s1_un_s2__un_s3__un_s4 = s1.union(s2,s3,s4)
print(s1_un_s2__un_s3__un_s4)


msg = '''
intersection of sets
two methods '&' and intersection
'''
print(msg)
print("Method 1 using '&' operator")
s1 = {1,2,3,4}
s2 = {1,5,6}
s1_i_s2 = s1 & s2
print(s1_i_s2)
print("Method 1 using intersection function")
s1_in_s2 = s1.intersection(s2)
print(s1_in_s2)
print("Unnion for more than 2 sets")
s1 = {1,2,3,4}
s2 = {1,5,6,2}
s3 = {2,7,8}
s4 = {1,9,2}
s1_i_s2__i_s3__i_s4 = s1 & s2 & s3 & s4
print(s1_i_s2__i_s3__i_s4)
s1_in_s2__in_s3__in_s4 = s1.intersection(s2,s3,s4)
print(s1_in_s2__in_s3__in_s4)


msg = '''
difference of sets
two methods '-' and difference
'''
print(msg)
print("Method 1 using '-' operator")
s1 = {1,2,3,4}
s2 = {1,5,6}
s1_d_s2 = s1 - s2
print(s1_d_s2)
print("Method 1 using difference function")
s1_di_s2 = s1.difference(s2)
print(s1_di_s2)
print("Unnion for more than 2 sets")
s1 = {1, 2, 3, 30, 300}
s2 = {10, 20, 30, 40}
s3 = {100, 200, 300, 400}
s1_d_s2_d_s3 = s1 - s2 - s3
print(s1_d_s2_d_s3)
s1_di_s2_di_s3 = s1.difference(s2,s3)
print(s1_di_s2_di_s3)


msg = '''
symmetric_difference of sets
two methods '^' and symmetric_difference
'''
print(msg)
print("Method 1 using '^' operator")
s1 = {1,2,3,4}
s2 = {1,5,6}
s1_sd_s2 = s1 ^ s2
print(s1_sd_s2)
print("Method 1 using symmetric_difference function")
s1_sdi_s2 = s1.symmetric_difference(s2)
print(s1_sdi_s2)
print("Unnion for more than 2 sets")
s1 = {1, 2, 3, 30, 300}
s2 = {10, 20, 30, 40}
s3 = {100, 200, 300, 400}
s1_sd_s2_sd_s3 = s1 ^ s2 ^ s3
print(s1_sd_s2_sd_s3)
try:
    s1_sdi_s2_sdi_s3 = s1.symmetric_difference(s2,s3)
except Exception as e:
    print("This is error for set.symmetric_difference only one arg")
    print(type(e).__name__,e)
    
msg = '''
isdisjoint
Determines whether or not two sets have any elements in common.
Return val : True if no common elements
'''
print(msg)
s1 = {1, 2, 3, 30, 300}
s2 = {10, 20, 30, 40}
print(s1.isdisjoint(s2))


msg = '''
issubset , '<='
Determine whether one set is a subset of the other.
Return Val : True if LHS is subset of RHS otherwise False
'''
print(msg)
s1 = {30, 300}
s2 = {10, 20, 30, 300}
s3 = {1,2,30}
s4 = {30, 300}
print(s1.issubset(s2))
print(s1.issubset(s3))
print(s1.issubset(s4))
print(s1 <= s2)
print(s1 <= s3)
print(s1 <= s4)

msg = '''
proper subset
<
'''
print(msg)
s1 = {30, 300}
s2 = {10, 20, 30, 300}
s3 = {1,2,30}
s4 = {30, 300}
print(s1 < s2)
print(s1 < s3)
print(s1 < s4)


msg = '''
issuperset , '>='
Determine whether one set is a superset of the other.
Return Val : True if LHS is superset of RHS otherwise False
'''
print(msg)
s1 = {10, 20, 30, 300}
s2 = {30, 300}
s3 = {1,2,30}
s4 = {10, 20, 30, 300}
print(s1.issuperset(s2))
print(s1.issuperset(s3))
print(s1.issuperset(s4))
print(s1 >= s2)
print(s1 >= s3)
print(s1 >= s4)

msg = '''
proper superset
>
'''
print(msg)
s1 = {10, 20, 30, 300}
s2 = {30, 300}
s3 = {1,2,30}
s4 = {10, 20, 30, 300}
print(s1 > s2)
print(s1 > s3)
print(s1 > s4)


msg = '''
update
s1.update(s2) and s1 |= s2 add to s1 any elements in s2 that s1 does not already have:
menas s1 = s1|s2(in memmory operarion will take place)
this can take more than one arguments(sets)
x1.update(x2[, x3 ...])
x1 |= x2 [| x3 ...]
'''
print(msg)
s1 = {10, 20, 30, 300}
s2 = {40, 300}
s1 |= s2
print(s1)
s1 = {10, 20, 30, 300}
s2 = {40, 300}
s1.update(s2)
print(s1)


msg = '''
intersection_update
x1.intersection_update(x2[, x3 ...])
x1 &= x2 [& x3 ...]
meaning : x1 = x1 & x2
'''
print(msg)
s1 = {10, 20, 30, 300}
s2 = {40, 300}
s1 &= s2
print(s1)
s1 = {10, 20, 30, 300}
s2 = {40, 300}
s1.intersection_update(s2)
print(s1)


msg = '''
difference_update
x1.difference_update(x2[, x3 ...])
x1 -= x2 [| x3 ...]
meaning : x1 = x1 - x2
'''
print(msg)
s1 = {10, 20, 30, 300}
s2 = {40, 300}
s1 -= s2
print(s1)
s1 = {10, 20, 30, 300}
s2 = {40, 300}
s1.difference_update(s2)
print(s1)

msg = '''
symmetric_difference_update
x1.symmetric_difference_update(x2[, x3 ...])
x1 ^= x2 [| x3 ...]
meaning : x1 = x1 ^ x2
'''
print(msg)
s1 = {10, 20, 30, 300}
s2 = {40, 300}
s1 ^= s2
print(s1)
s1 = {10, 20, 30, 300}
s2 = {40, 300}
s1.symmetric_difference_update(s2)
print(s1)

