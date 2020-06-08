hrs = input("Enter Hours:")
rate = input("Enter Rate:")

try:
    h = float(hrs)
    r = float(rate)
except:
    print("Enter the correct Number")
    quit()

def computepay(h, r):
    diff = 0
    if h > 40:
        diff = h-40
        h = 40
        pay = (h+(diff *1.5))*r
        return pay
    else:
        pay = (h*r)
        return pay

print('Pay', computepay(h, r))
