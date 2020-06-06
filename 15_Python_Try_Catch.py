#Try
'''It checks the error in the block of code'''

#Exception
'''Handles the error'''

#Finally
'''runs teh defaukt code, independent of try and catch
'''

try:
	print(x)
except:
	print("Exception occured")
	

try:
	print(y)
except NameError:
	print("y var not defined")
except:
	print("Exception occured")
	
try:
	print("Hiii")
except:
	print("y var not defined")
else:
	print("Everything works fine")
	
#Finally
try:
	print(m)
except:
	print("m var not defined")
finally:
	v = 13
	tx = "Try and except got completed, and the code of finally ran successfully {}."
	print(tx.format(v))