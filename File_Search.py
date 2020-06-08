myfile = open('file.txt', 'r')
for line in myfile:
    if line.startswith('From:') :
        print(line)
