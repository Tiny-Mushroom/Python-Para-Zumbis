x = 80000
y = 200000
t = 0
while y >= x:
    x = x + (x * 0.03)
    y = y + (y * 0.015)
    t = t + 1
print(t)
