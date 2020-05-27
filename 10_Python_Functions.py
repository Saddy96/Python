#FUNCTIONS
'''Code to run once it is called'''
#we can pass a Var to it known as Parameters called as ARGUMENTS
#Also, it returns some data as result

#use def to create a function in python:

#Without Argemetns
def myFirstFunction():
	print("My Name is : RAJNI" )
print("Without Arguments: ")
myFirstFunction()


#With Argements also called as args in python
'''use comma to separate various parameters of argements'''
def mySecondFunction(name):
	print("My Name is : " + name)	
	
print("With Arguments: ")
mySecondFunction("RajniKanth")

#Difference between PARAMTER AND ARGUMENT
'''
PARAMTER = name passed while creating a function
ARGUMENT = Value passed while calling the function
'''

#ARBITARY arguments
'''When we are not sure
about the no of input to a function we can use arbitary function as *args'''
# *args will take tuple as input arguments

def arbitaryInputFunction(*fruitnames):
	print("My Name is : " + fruitnames[1])	
	
print("With arbitary Arguments: ")
arbitaryInputFunction("apple", "orange", "Pineapple")

#KEYWORD Argument
'''
when we want to pass the key with value while calling the function then it is called as keyword arguments
and we don't have to think about the order at that time'''
def keywordArgumentFunction(fruit3, fruit1,fruit2):
	print("My best fruit is : " + fruit3)	
	
print("With Keyword Arguments: ")
keywordArgumentFunction(fruit2 = "apple", fruit3 = "orange", fruit1 = "Pineapple")

#KEYWORD Arbitary Argument
'''
when we are not sure the no of paramters of the keyword arguments
and we don't have to think about the order at that time'''
def keywordArbitaryArgumentFunction(**fruit):
	print("My next best fruit is : " + fruit["fruit1"])	
	
print("With Arbitary Keyword Arguments: ")
keywordArbitaryArgumentFunction(fruit2 = "apple", fruit3 = "orange", fruit1 = "Pineapple")

#Default Parameter
'''
When no values are passed it will
take the default value defined while creating the function'''
def defaultParamDefined (rollNo = 13):
	print("My Rool no is " + format(rollNo))
	
defaultParamDefined(1)
defaultParamDefined(45)
defaultParamDefined() # will print the default value of the param as there is no value passed

#PASS
'''used to keep the empty content in a funtion'''

#RETURN VALUES
'''Function to return some values'''
def returnValue (input):
	return input*input

print(returnValue(5))

#RECURSION
'''it can call teh same function inside it'''
#it calls itself
#Loop through data to reach a result

def try_recursion(inputVal):
	if (inputVal > 0):
		result = inputVal + try_recursion(inputVal-1)
		print(result)
	else:
		result = 0
	return result
print("\n\nRecursion Values: ")
try_recursion (4)


#LAMBDA
'''its a small anonymous function'''
#Anonmous Meaning = no function name
#Can take n no of arguments
#Can only have one experesions

#SYNTAX
'''
lambda arguments: expression
'''
x = lambda m : m + 3
print(x(4))

x = lambda m, n, o, p : m + n + o+ p
print(x(2,2,2,2))

def myfunc(n):
  return lambda a : a + n

mydoubler = myfunc(2)

print(mydoubler(11))