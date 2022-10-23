x, y = float(input()), float(input())
fl = 0
if x > 0 and abs(y) <= 1:
    if x * x + y * y <= 1:
        fl = 1
    if x - 1 <= y <= 1:
        fl = 1
if fl:
    print("Yes")
else:
    print('No')
