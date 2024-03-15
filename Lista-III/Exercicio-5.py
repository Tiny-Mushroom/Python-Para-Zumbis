a = int (input('Digite o primeiro numero '))
b = int (input('Digite o segundo numero '))
while (a % b) > 0:
    r = a % b
    a = b
    b = r
print(b)
