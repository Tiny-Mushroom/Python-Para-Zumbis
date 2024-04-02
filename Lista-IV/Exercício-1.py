import random
randint = random.sample(range(1, 101), 10)
print("sample:", randint)

maxint = 0
minint = 101

for i in randint:
    if i > maxint:
        maxint = i
    if i < minint:
        minint = i
print("Max:", maxint)
print("Min:", minint)