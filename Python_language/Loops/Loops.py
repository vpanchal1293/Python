count = 0
while (count < 9):
    #print ('The count is:', count)
    count = count + 1

for i in range(10):
    #print ('The count is:', i)
    pass
print ('The count is:', i)



'''
While Else:
else will be executed if there is no break in look
'''
print('\n'*2)
print("Example of while, no break, hence else will executed")
count = 0
while (count < 9):
    print ('While loop The count is:', count)
    count = count + 1
else:
    print("End Of while loop")
print('\n'*2)


'''
while else 
else will not be executed if there is break in look
'''
print('\n'*2)
print("Example of while, with  break condition , hence else won't executed")
count = 0
while (count < 9):
    print ('While loop The count is:', count)
    count = count + 1
    if (count == 3):
        print('Here is break')
        break
else:
    print("End Of while loop")
print('\n'*2)


for i in range(10):
    print ('For loop The count is:', i)
else:
    print ('End of for loop')
