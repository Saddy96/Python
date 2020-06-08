fname = input('Enter teh filename : ')
try:
    myfile = open(fname)
except:
    print('Can\'t open the file either it\'s not avaiable to wrong file name')
    quit()

count = 0
for line in myfile:
    if line.startswith('Subject'):
        count = count + 1

print('There are', count, 'lines that has Subject: as initials in file ', fname)
