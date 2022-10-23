x, y = float(input()), float(input())
fl = 1 if (x * x + y * y <= 1 and (y >= x or (y <= x <= 0))) else 0
if fl:
    print('Yes')
else:
    print('No')
