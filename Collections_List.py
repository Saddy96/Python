#colections - it holds more than one thing (like more than one var)

'''Lists are denoted by [ ]'''

listdata = [54, 35, 56, 67, 78]
for i in listdata:
    print(i)
print('Done with printing all the values of lists')

friends = ['John', 'Don', 'Cook']
for friend in friends:
    print('Very welcome :', friend)

print('Done!')

#Get the respective Values:
print(friends[1])

#ists are Mutable/Changeable
friends[1] = 'Arys'

#Length of lists
print(len(friends))

print(range(len(friends)))

#Get the position
'''Counted Loop'''
for i in range(len(friends)):
    friend = friends[i]
    print('Happy Here :', friend)

#Concateating/Add Lists
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

#Slicing
d = c[1:3] # or c[:3]
print(d)

xy = list()
type(xy)
#Methods of lists
print(dir(xy))

#Building a lists
ld = list()
ld1 = []
#print(type(ld))

'''Use append method to add an element'''
ld.append('apple')
ld.append(78)
print(ld)

#using in to check if some thing is there
'''in'''
s = 78 in ld
print(s)

'''Not in'''
f = 'banana' not in ld
print(f)

#Ordering the Lists
friends.sort()
print(friends)

#Other built in function
nums = [9, 78, 45, 5, 23, 5, 7]
length = len(nums)

print(range(len(nums)))
print('nums length: ',length)

print(max(nums))

print(min(nums))

print(sum(nums))
