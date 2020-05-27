#Python has two types of loops:
	#While
	#For

# WHILE
'''While loop run till the 
certain condition is true'''
i=1
while i < 5:
	print(i)
	i += 1
# Always increase the variable by 1 else it will run in infinte loop

#Break statement
'''To stop teh loop
at any point of time
use break command'''

while i < 9:
	if i == 5:
		break;
	print (i)
	i += 1


print("Next is Continue statement value")
#Continue 
'''it will skip the current loop
and move to next loop'''
a = 0
while a < 9:
	a += 1
	if a == 5:
	  continue
	print(a)

# FOR LOOP
'''it checks/itterate over all the value/sequence
mentioned'''
listFruit = ["Orange", "Banana", "Pineapple"]
for x in listFruit:
	print(x)
	Text = "Loop through the String {}" 
	print(Text.format(x))
	for x in x:
		print(x)

#Break in For Loop
'''Stop the loop at specific condition'''
IndexNo = 1
for x in listFruit:
	Text = "{0} index String is {1}" 
	print(Text.format(IndexNo,x))
	
	if x == "Banana":
		break
	IndexNo += 1
	
print("Final Index Value: " + format(IndexNo))

#Range in For Loop
'''To run the for loop
for specified no of times use range() func'''
for x in range(5):
	print(x) # Will start from 0 to 4
#It has default range as 0 if not provided

print("Show all the value starting from 3 to 6")
for x in range(3,7):
	print(x)

# Default increment of range is 1 to use more follow as shown below

print("Show all the value 10 and 100 and increment by 10")
for x in range(10,100, 10):
	print(x)
	
#Else in for loop
'''code to be excuted once the for loop is over'''
for x in listFruit:
	print(x)
else:
	print("Printed all the Value")

