import random

vectin1 = random.sample(range(1, 101), 10)
vectin2 = random.sample(range(1, 101), 10)
vectout = []
cnt = 0

print("Input 1:", vectin1)
print("input 2:", vectin2)

while cnt < 10:
    vectout.append(vectin1[cnt])
    vectout.append(vectin2[cnt])
    cnt = cnt + 1

print("Output:", vectout)
