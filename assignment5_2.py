count = 0
largest = None
smallest = None
while True :
    inp = input('Enter your no: ')
    count = count +1
    if inp == 'done':
        break
    try:
        intno = int(inp)
    except:
        print('Invalid input')
        continue

    if largest is None:
        largest = intno
        smallest = intno
    elif intno > largest:
        largest = intno
    elif intno < smallest:
        smallest = intno

if count == 1:
    print('No values Entered')
else:
    print('Maximum is',largest)
    print('Minimum is',smallest)
