'''Split breaks a string into parts
and produces a list of strings. We
think that as a word, we can
access a particular word or
loop through all the works'''
abc = ' Welcome Home San'
stuff = abc.split()
print(stuff)
print(len(stuff))

for word in stuff:
    print(word)

fhand = open('file.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    words = line.split()
    print(words)

m = 'From: stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
wordsdata = m.split()
email = wordsdata[1]
piecedata = email.split('@')
print(piecedata)

print(piecedata[1])
