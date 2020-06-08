myfile = open('file.txt', 'r')
count = 0
for dat in myfile:
    count = count + 1
    print(dat)

print(count)
