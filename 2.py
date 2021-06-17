list1 = [i for i in range(1000)]
print(list1)

#list2 = [i for i in xrange(1,6)]
#print(list2)
# I found out that in python 3 version the xrange function does not exits.
'''
range() and xrange() are two functions that could be used to iterate a certain number of times in for loops in Python. 
In Python 3, there is no xrange , but the range function behaves like xrange in Python 2.
If you want to write code that will run on both Python 2 and Python 3, you should use range().
'''