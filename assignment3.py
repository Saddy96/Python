hrs = input("Enter Hours:")
rate = input("Enter Rate:")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("Enter the correct Number")
    quit()


diff = 0
if h > 40:
    diff = h-40
    h = 40
    pay = (h+(diff *1.5))*r
else:
    pay = (h*r)
print(pay)
