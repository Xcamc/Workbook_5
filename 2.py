def chet(x):
    if x % 2 == 0:
        return 1
    else:
        return 0


a, b, c = int(input()), int(input()), int(input())
if chet(a) + chet(b) + chet(c) >= 2:
    print('Yes')
else:
    print('No')
