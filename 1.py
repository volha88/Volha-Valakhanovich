х = float(input('x = '))
n = int(input('n = '))
s = x
for i in range(2, n+1):
    x *= -x * x / ((2 * i - 1) * (2 * i - 2))
    s += x
print(s)
