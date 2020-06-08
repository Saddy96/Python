fh = open('AssignmentText8_4.txt')
listdata = list()
for line in fh:
    linenew = line.rstrip()
    linewords = linenew.split()
    for i in linewords:
        if i in listdata:
            continue
        else:
            listdata.append(i)

finaldata = listdata.sort()    
print(listdata)
