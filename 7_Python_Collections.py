#There are 4 collection data types in python
#List = it is ordered and chnageable, allows duplicate members
#Tuple = it is ordered and unchangeable, allows duplicate members
#Set =  it is unordered and unindexed, no duplicate members
#Dictionary = unordered, indexed and changeable, no dupliacte members

createdlist = ["Pant", "Shirt", "Tie"]
print(createdlist)
print(type(createdlist))

#Access Items
'''use [] to acces the items'''
print(createdlist[0]) # Will print Pant

#Negative IndexError
''' Start reading from tehe end'''
print(createdlist[-1]) # Will print Tie

#Read between the range indexes

newCreatedList = ["Pant", "Shirt", "Tie", "Shoe", "Belt", "Socks"]
print(newCreatedList[2:5]) # Will print from Tie till Belt as 5 index is excluded

#Change item Value
newCreatedList[2] = "T-Shirt"
print(newCreatedList) # Will print list with replaced value of Tie to T-Shirt

#Loop through list

for x in createdlist:
	print (x)
	
#Check is an item is there in the list
if "Tie" in newCreatedList:
	print("Yes Tie is there in the list")

#Append
'''To add an item to an end in the list
use append'''
newCreatedList.append("Jeans")
print(newCreatedList)

#insert
'''To add at any specific index use insert'''
newCreatedList.insert(4,"Add at 4th Index")
print(newCreatedList)

#Removing or deleting an item
'''3 ways to remove an item from list'''
#remove() = removes the provided text from the list
newCreatedList.remove("Add at 4th Index")
print(newCreatedList)

#pop(), removes the specific index text and if no index provided then removes last index
newCreatedList.pop(4) # removes Belt
newCreatedList.pop() # removes last item as no index provided
print(newCreatedList)

#del(), removes the spefied index item
del newCreatedList[1] 
print(newCreatedList)


#clear method empties the list
createdlist.clear()
print(createdlist)


#TUPLES
'''collection which is ordered but unchangeable, it is written with () brackets'''
thistuple = ("Pant", "Shirt", "Tie")
print(thistuple)
print(type(thistuple))

#Acces Tuples
'''Same way as done in list'''
print(thistuple[1]) # print Shirt

#Change Tuple Values **** its unchangeable
#but u can change it by converting it to list and do the changes and then change it again to tuple

#Loop through tuple
for x in thistuple:
	print(x)
	
#Single Tuple item , Put a comma at the end so it will take as a single tuple else it will become str
singletuple = {"apple",}
print(singletuple)
print(type(singletuple))

#Delete tuple completely
#use del singletuple to delete singletuple


#SETS: Unordered and Unindexed, it is written with {}
thisset = {"Pant", "Shirt", "Tie"}
print(thisset)
print(type(thisset))

#Note: Sets are unordered, so u can't make sure the order the items will appear
# Once a set is created, you cannot change its items, but you can add new items.

#Dictionary: unordered, changeable, indexed. it is written with {} and they have key and values
thisdist = {
			"brand": "CK",
			"model": "007",
			"year": "1998"
}

print(thisdist)
print(type(thisdist))

#Access items:
'''using key name inside hte brackets'''
print(thisdist["model"])
#Can also be done using get()
#Same as above
print(thisdist.get("model"))

#chaning the items
thisdist["year"] = 1999
print(thisdist)

#Loop through the dist
''' will print all the key'''
for x in thisdist:
	print(x)
	
''' to get key vlues'''
for x in thisdist:
	print(thisdist[x])
	
#or use .values() method
for x in thisdist.values():
	print(x)

#Loop through both keys and values use items()
for x,y in thisdist.items():
	print(x,y)
	
#To make a compy of any above colection use below method
mydist = thisdist.copy()
print(mydist)