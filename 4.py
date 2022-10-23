import math as m

x, y = float(input()), float(input())
if m.sin(x) <= y and 0.5 >= y >= 0:
    print("Yes")
else:
    print('No')
