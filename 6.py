x, y = float(input()), float(input())
fl = 1 if (x > 0 and abs(y) <= 1 and (x * x + y * y <= 1 or x - 1 <= y <= 1)) else 0
if fl:
    print("Yes")
else:
    print('No')
