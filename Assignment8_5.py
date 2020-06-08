fh = open('AssignmentText8_5.txt')
count = 0
for line in fh:
    line.rstrip()
    if line == '':
        continue
    if line.startswith('From '):
        count = count + 1
        words = line.split()
        print(words[1])
print('There were', count, 'lines in the file with From as the first word')
