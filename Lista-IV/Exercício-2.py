import random

randint = random.sample(range(1, 101), 20)

evenint = []
oddint = []

for i in randint:
    if i % 2 == 0:
        evenint.append(i)
    if i % 2 != 0:
        oddint.append(i)

print("sample:", randint)
print("Even:", evenint)
print("Odd:", oddint)