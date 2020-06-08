score = input('Enter the Score :')
try:
  intscore = float(score)
except:
  print("Input Correct Data")
  quit()

if intscore > 0 and intscore < 1.0:
    if intscore >= 0.9:
        print('A')
    elif intscore >= 0.8:
        print('B')
    elif intscore >= 0.7:
        print('C')
    elif intscore >= 0.6:
        print('D')
    else:
        print('F')
else: print('Out of Range score')
