text = "X-DSPAM-Confidence:    0.8475";
leng = len(text)
letter0 = text.find(' ')

data = text[letter0:leng]
val = data.lstrip()
print(float(val))
