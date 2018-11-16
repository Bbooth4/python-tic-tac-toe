from random import shuffle, randint

print('hello world', 2 + 1, 50 % 10, 0.1+0.2-0.3, type(1))

# types - int, float, str, list, dict, tup, set, bool (True/False)
# && = and || = or

a = 'test string'

# a[start:end:skip/step]

print(a[1:8:2])

# can be used to reverse a string
print(a[::-1])

q = 'string'
q = 'name'

print(q)

# indexes in {} decide the order of insertion, or just choose the order based on where they are in the list
print('Strings are {1} and inserted {0} plus {bonus:1.5f}'.format('again', 'inserted', bonus=0.124345932))

print(f'Hello {q}')

# .splice() exists

list1 = [1, 2]
list2 = [3, 4, 5]
list = list1 + list2

# easy array concatenation
print(list)

# .append() === .push(), .pop() is the same but you can added indexes to .pop()

list.insert(1, 'word')

print (len(list), list, list.index(3))

object = {
  'a': 1,
  'b': [1, 2, 3]
}

o = {1: 1, 2: 2}
print(o)

print(object['b'][1])
print(object.keys())
print(object.values())
print(object.items())

# immuntable list
t = (1, 2, 3, 3)
print(t.count(3), len(t))
# returns the first index location of 3
print(t.index(3), t[0])

s = set()
s.add(1)

# all values within must be unique
print(s)

ss = {1, 2}

print(type(ss))

set_array = [1, 2, 2, 2, 2, 3]
# all values within a set must be unique so the duplicates get filtered out
print(set(set_array))

myfile = open('test.txt')

print(myfile.read())
# this resets the cursor so that it can read the same file multiple times
myfile.seek(0)
# creates an array of lines from the file
print(myfile.readlines())

# in order to ensure it is closed so that it is usuable in other places, otherwise it will think that python is still using it
myfile.close()

# this will auto-close the file once you are done with it
# mode=r for read
# mode=w for write
# mode=a append, adds to the end of a file
# mode=r+ reading and writing
# mode=w+ writing and reading, overwrites existing files or creates a new file

with open('test.txt') as content:
  contents = content.read()

print(content)

with open('test.txt', mode='a') as a:
  a.write('\nFourth Line')

with open('test.txt', mode='r') as r:
  print(r.read())

with open('test2.txt', mode='w') as w:
  print(w.write('Test 2'))

# falsy in python
# None
# False
# 0
# 0.0
# 0j
# Decimal(0)
# Fraction(0, 1)
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# '' - an empty str
# b'' - an empty bytes
# set() - an empty set
# an empty range, like range(0)
# objects for which
# obj.__bool__() returns False
# obj.__len__() returns 0

if True:
  print(True)
elif False:
  print(False)
else:
  print('Error')

array = [1, 2, 3] 
a = [1, 2, 3, 4] 
tup = [(1, 2, (1, 2)), (3, 4, (1, 2)), (5, 6, (1, 2))]
obj = {1: 'a', 2: 'b', 3: 'c'}

for item in array:
  print(item)

for a, b, (c, d) in tup:
  print(a, b, c, d)

# iterating a dtionary does not guarantee that the items will list out in order
for key, val in obj.items():
  print(key, val)

# defaults to just the keys
for k in obj:
  print(k)

for v in obj.values():
  print(v)

# break (end), continue (move on), pass (does nothing)
i = 0
while i < 5:
  i += 1
  if i == 4:
    break
  if i == 1: # skips printing True when i == 1
    continue
  print(True)
else:
  print(False)

# prints 2 - 5 skipping by 2 (like i += 2 instead of i++)
for num in range(2, 5, 2):
  print(num)

# creates tuples, first is index, second is value
for i, num in enumerate(array):
  print(i, num)

# creates a new tuples, must be the same length
for i in zip(array, tup, array):
  print(i)

# check if a value is in an array, string, dictionary keys
print(2 in array)
# check a dictionaries values
print('a' in obj.values())

print(min(array), max(array))

mylist = [1, 2, 3, 4, 5, 6]
shuffle(mylist)
print(mylist)

#selects a random integer
print(randint(0, 100))

# always returns a string unless otherwise specified
# alert() equivalent
# result = input('Enter a number: ')

# print(int(result))

# can add low within it as well
newlist = [i for i in 'word']
print('comprehension', newlist)

celcius = [0, 10, 20, 34.5]

# the first argument before the for is equivalent to what you would have appended 
fahrenheit = [(9/5*temp+32) for temp in celcius if temp != None]
print(fahrenheit)

# with else statement
res = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(res)

# nested for one line version multi-line
# nested_for = [x*y for x in [1, 2, 3] for y in [4, 5, 6]]
nested_for = [
  x*y
  for x in [1, 2, 3]
  for y in [4, 5, 6]
]

print(nested_for)

# any possible parameters require default values, no optional parameters
def func(val):
  '''
  DOCSTRING: used to describe the function
  INPUT: nothing
  OUTPUT: num
  '''
  return val

func(1)

def sums(*args):
  print(sum(args))

sums(1, 2, 3, 4, 5)

def keyvalue(**kwargs):
  print(kwargs)
  if kwargs['num'] > 3: print('Greater than 3')
  else: print('Less than 3')

keyvalue(num=2)

def double(n):
  return n*2

for item in map(double, array):
  print(item)

# returns a map object, can be iterated over but can't log it's contents
doubled_nums = map(double, array)
print(doubled_nums)

def check_even(num):
  if num % 2 == 0:
    return num

# returns a filter object which is filtered by the provided function
print(filter(lambda num: num % 2 == 0, array))

# lambda functions are anonymous functions like () => {} in js
square = lambda num: print(num ** 2)

square(5)

# help() returns information about a function, not methods
# help(map)
