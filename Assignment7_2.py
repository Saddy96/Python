# Use mbox-short.txt as the file name
fname = input("Enter the file name: ")
fh = open(fname)
filterconst = 'X-DSPAM-Confidence:'
output = 0.0
count = 0
for line in fh:
    if line.startswith(filterconst):
        data = line.split()
        val = float(data[1])
        count = count + 1
        output = output + val

print('Average spam confidence:'', output/count)
