from sys import argv

a, b, c = int(argv[1]), int(argv[2]), int(argv[3])
d = b**2-4*a*c
if d > 0:
    x1 = -b+(d**0.5)/(4*a*c)
    x2 = -b-(d**0.5)/(4*a*c)
    print(f"X1 = {x1:#.2f}, X2 = {x2:#.2f}")
elif d == 0:
    x1 = -b+(d**0.5)/(4*a*c)
    print(f"X = {x1:#.2f}")
else:
    print("Действительных корней нет")
