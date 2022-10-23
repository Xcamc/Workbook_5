x, y = float(input()), float(input())
if x * x + y * y <= 1 and (y >= x or (y <= x <= 0)):
    print('Yes')
else:
    print('No')
