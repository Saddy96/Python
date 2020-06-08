# Use words.txt as the file name
fname = input("Enter the file name: ")
fh = open(fname)

#By using the read method
'''fileString = fh.read()
convertedupper = fileString.upper()
print(convertedupper.rstrip())'''


#or
for line in fh:
    linenew = line.rstrip()
    print(linenew.upper())
