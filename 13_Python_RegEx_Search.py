#To search a patern in the text use RegEx library

import re

txt = "You are the best"
#if the specified charather there at the begining
x = re.search("\AYou", txt)

#if it starts with
y = re.search("^You", txt)

print(x)
print(y)