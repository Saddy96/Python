#Data Types:
'''Built-in 
Data types of
Python'''
#Text = str
#Numeric = int, float, complex
#Sequence = list, tuple, range
#Mapping = dict
#Set = set, frozenset
#Boolean = bool
#Binary = bytes, bytesarray, memoryview

#to get the type of the variables use type()
a = 5
print(type(a))

#To set the specific type of the variables use exact type of the datatype
b = complex(1j)
print(b)
print(type(b))

#Number Data Types:
'''There are 3
types of Number Data types:
int,
float,
Complex'''

#Int
'''Int, or integer, is a whole number,
positive or negative,
without decimals, of unlimited length'''
c = 12 #int
d = 123456789012367 #int
e = -12334567
print(type(c))
print(type(d))
print(type(e))

#Float
'''any number, positive, negative containing one or 
more decimal places'''
f = 0.5
g = -2.56
print(type(f))

#Complex
'''written with j as
inmaginary part'''
h = 3+2j
print(type(h))

#Type Conversion/Casting
''' convert to differnt type using its type method like
int(), float(), complex()'''
i = 56
j = 3.9
k = 2+5j

#Convert from int to float
print(float(i))
print(type(i))

#Convert from float to int
print(int(j))
print(type(j))

#NOTE: Complex can't be converted into any other data type

#Multi Line String/Str
l = '''It has multi-
line
string with Value'''
print(l)

#Strings are Arrays
''' All the strijng stored are
stored as an array and they can be accesed using
[]'''
m = "The Times of India"
print("Will Print the e of The as e is the 2 nd character considering 0 indexing : " + m[2]) # Will print e of The

#Slicing
'''Removing the specific characters from the variables
or getting teh specific character within the 
range provided'''
n = "The Times Of India"
print("Will print the character starting from 4 and till 10 : " + n[4:12])

#Negative Indexing
'''Removing the character by 
starting the indexing from the end'''
o = "The Times of India"
print(o[-7:-1])
# String Length
'''Use len(), to get the
length of the String'''
print("Print the length of String : "+ str(len(o)))

#String Methods:
#strip()
'''This will remove the any white spacing from
there in thhe starting of the tezt or end'''
p = "  Hello             World        "
print(p.strip())

#Lower Method lower()
'''Converts the the text
into lower letter'''
q = "LOWER"
print(q.lower()) # Will convert to lower Letter

#Upper Method upper()
'''Converts the the text
into Upper letter'''
r = "upper"
print(r.upper()) # Will convert to UPPER Letter

#Replace Method replace()
'''replace a character of the
string to another'''
s = "Boll"
print(s.replace("l", "w")) # Will replace all l to w

#Split Method split()
t = "Hello World!"
print(t.split())

#Check String
'''To check a certain charatcer in
a string use "in" or "not in" '''
txt = "screw.pvz"
check = ".pvz" in txt
print(check)
#Or Use Not in
checknotin = "win" not in txt
print(checknotin)

#String Concatinate
first = "Hello"
Second = "World"
print(first + " " + Second)

# We can't add a number to string
'''The format() method takes the passed arguments, 
formats them, and places them in the string where 
the placeholders {} are'''
no = 24
String = "My age is : {}"
print(String.format(no))

quant = 23
itemno = "Pizza"
price = 46.7
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quant, itemno, price))

'''use index based
options to place the exact value on the
required place'''
myorder = "I want to pay {2} dollars for {0} pieces of {1}"
print(myorder.format(quant, itemno, price))

#Escape Characters: use \
'''Use Escape method to put the
illegal character inside the string'''
textcorrect = "I am a lone survivour \"The Survivour\" from the last accident"
print(textcorrect)


#BOOLEAN
print(10>8) #Will print True

#bool()
'''checks whether the var has a value or not'''
vale = ""
no2 = 13
print(bool(vale))
print(bool(no2))