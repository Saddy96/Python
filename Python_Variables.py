#This code provides the explanation of variables options available in python
'''Python doesn't require
to have a var to be decalred'''
'''whenever we assign any value to it it becomes a variable'''
x=5
y="Contains text"
print(x) #Prints x varaible
print(y) #Prints y varaible
#Variables are container to store a data value

'''Variables in python doesn’t 
require to be declared
with any particular type and can 
even change when they have been set'''
a=4 # a is of type int
a="changed" # a is now of type string
print(a) # prints updated value of a

#String variables can be decalred either by using single or double quotes
b="John"
#sama as
b='John'
print(b)

# MULTIPLE VARIABLES
'''Python allows you to assign 
values to multiple variables 
in one lin'''
c,d,e = "First Text", "Second Text", "Third Text" 
print(c)
print(d)
print(e)

'''or you can assign a value
to differnt variables'''
f=g=h = "Same Text"
print(f)
print(g)
print(h)

#OUTPUT VARIABLE
'''Python print statement to output a
variable. To combine both
text and variable python uses+'''
i = "Addition"
print("This text ia an of printing a variable value " + i )

#GLOBAL VARIABLES
'''Variables which are created 
outside a function are
known as global variable'''
j = 'AWESOME'
def myfunc():
 print("python is - "+j)

myfunc()

#GLOBAL VARIABLES AND LOCAL VARIABLES
'''If you create a varaible with the same name as
global varaible insode the function, then
this variable will be local and can only
be used inside the funtion
The Global variable with the same name will remain
same as it was and with the same value'''
k = 'AWESOMENEW'
def myfuncnew():
	k = "AWOSOME CHANGED TO GOOD"
	print("python is - "+k)
myfuncnew()
print(k)

#GLOBAL Keyword
'''When avariable is created inside the function
then it is called as local and it will be used only inside
the function'''
'''to create a global varibale indide 
the function use global'''

def myfuncwithGlobalVar():
	global l
	l = "Global variable defined inside the function"
	
myfuncwithGlobalVar()
print(l)

#Changing the Value of GLOBAL VARIABLE
'''use global inside the functionto change the 
value of teh variable inside the function'''
def myfuncGlobalValueChange():
	global x
	x="Changed from 5 to New Value"

myfuncGlobalValueChange()
print("x value chanegd to new using the global keyword - " + x)
