# open the txt file
myfile = open('file.txt', 'r')
for line in myfile:
    #Remvoving the \n from the text
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)
