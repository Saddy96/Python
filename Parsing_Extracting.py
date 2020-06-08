data = 'From abc.def@gmail.com Sun Jun 7 2020'
atpos = data.find('@')
print(atpos)

#Will search the first occurence
sppos1 = data.find(' ', atpos)
print(sppos1)

#Will search the occurence after atpos (@)
sppos = data.find(' ', atpos)
print(sppos)

extrctdata = data[atpos+1 : sppos]
print(extrctdata)
