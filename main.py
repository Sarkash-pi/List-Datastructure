'''
Creating Lists
'''

# List items are enclosed in square brackets
# Lists are ordered
# Lists are mutable
# List elements do not need to be unique.
# Elements can be of different data types.

# list = []
# list = [1,2,3]
# list = ['Orange', 'pear', 'Apple', 'Banana']
# list = [1, 'Hello', '6.0']
# print(list)


'''
List Indexing
'''

# fruits = ['Orange', 'Apple', 'Pear', 'Apple', 'Banana']
# print(fruits[2])

# We have list inside a list and for print we should have two square brackets to call it out
# fruits = ['Orange', 'Apple', ['Pear', 'Apple', 'Banana']]

# print(fruits[2][2])

'''
How to slice list in python
'''

# fruits = ['Orange', 'Apple', 'Pear', 'Apple', 'Banana']
# print(fruits[:])
# print(fruits[1:4])
# print(fruits[:-2])
# print(fruits[-2:])
# print(fruits[::3]) #doubl;e collom will skip a position/ every second or thirt etc
# print(fruits[::-1]) # it is reverse the list

'''
Add elements to a list
'''

fruits = ['Orange', 'Apple', 'Pear', 'Apple', 'Banana']
# fruits[0] = 'Berries'

# print(fruits)

# fruits[1:4] = ('Mandarins', 'Peaches', 'Plims')
# print(fruits)

# fruits.append('Limes') # adding an element
# print(fruits)

'''
Remove or delete list items
'''

# fruits = ['Orange', 'Apple', 'Pear', 'Apple', 'Banana']

# del fruits[0]
# print(fruits)

# del fruits[1:5]
# print(fruits)

# del fruits   # delete the list completeley
# print(fruits)

'''
Python list methods
'''

# print(help(dir)) #using help
# print(dir(list)) # usnig dir to check out to know what we can do to list, etc
# print(help(list.index))
# use dir to know all the mthods that we can do and help to find out about one od them

# fruits = ['Orange', 'Apple', 'Pear', 'Apple', 'Banana']
# fruits.append('Cashew')

# fruits.insert(0, 'Guava') #we add before the index and it's not replacing the value
# fruits.insert(3, 'Kiwi')
# print(fruits)

#======================

# print(help(list.clear))

# fruits = ['Orange', 'Apple', 'Pear', 'Apple', 'Banana']
# fruits.clear()
# print(fruits)

#======================

# fruits = ['Orange', 'Apple', 'Pear', 'Apple', 'Banana']
# # fruits.pop(1)
# # fruits.pop(0)

# # print(fruits.index('Pear')) #index to find out the index position

# #to pop an item without knowing the IndexError
# pos = fruits.index('Banana')
# fruits.pop(pos)

# print(fruits)

#======================

# fruits = ['Orange', 'Apple', 'Pear', 'Apple', 'Banana', 'Banana', 'Banana', 'Banana']

# print(fruits.count('Apple'))

# result = {}
# for x in fruits:
#   result[x] = fruits.count(x)

# print(result)

# # in future we gonna use easier way... using modules
# from collections import Counter
# print(Counter(fruits))

#========================

'''
List memebership test
'''

# fruits = ['Orange', 'Apple', 'Pear', 'Apple', 'Banana', 'Banana', 'Banana', 'Banana']

# print('Orange' in fruits)
# print('Orange' not in fruits)