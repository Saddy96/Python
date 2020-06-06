#Python follows OOPS concept or it is an OOP language

'''Eveything created in Python
is an Object, with its properties and methods.
'''

#A Class is like an object conctrcutor, or a "blueprint" for creating an object


#Class Creation
class MyNewClass:
	x = 5

#Creating various objects with the above created class
objectA = MyNewClass()

print(objectA.x)

#_intit_() Function
''' it's an inbuilt function
'''
#whenever any class gets created it contains the builtin function
#So all classes contains this function, it gets executed when a class is being initiated

class Student:
	def __init__(self,name,age):
		self.name = name
		self.age = age
		
StudentObject = Student("Arya", 15)
print("Name of the Student : " + StudentObject.name)
print(StudentObject.age)

#Objects can also have the Methods
class person:
	def __init__(self,Roll,Name):
		self.Roll = Roll
		self.Name = Name
	
	def myfunc(self):
		print("Hello my name is : "+ self.Name)

		
p1 = person(15, "John")
p1.myfunc();

#SELF param is refernce to the current instance of the class, is used to access the variables that belongs to the class

#We can use any name for SELF, but it has to be the first parameter of the function

class Person1:
	def __init__(myparam, name, age):
		myparam.name = name
		myparam.age = age
		
	def func(myparam):
		print("My name is : " + myparam.name)

P2 = Person1("DON", 56)
P2.func()

#Modify Object Params

P2.age = 12
print(P2.age)

#Delete the Object Properties
del P2.age

#Delete Object

del P2



#INHERITANCE:
'''its a way of calling a class inside another class and gets all the methods and properties'''

#Main Class/Base Class is being is the class being inherited

#Child CLass: Class that inherits from another class

#Parent Class
class Text:
	def __init__(mainTextParam, fname, lname):
		mainTextParam.fname = fname
		mainTextParam.lname = lname
	
	def printFunc(mainTextParam):
		print(mainTextParam.fname, mainTextParam.lname)
		
TextObj = Text("Don", "Bradman")
TextObj.printFunc()

#Child Class
class student1(Text):
	pass
	
v = student1("Mike", "Tyson")
v.printFunc()
	
#Add init() function in child class
		
class student2(Text):
	def __init__(mainTextParam, fname, lname):
		pass
'''after adding a init() func in child class 
it will no longer inherit the properties of parent class'''




