repeat = int(input("Quantos numeros você quer calcular? "))
x = 0
f = 1
if repeat < 3:
    while x < repeat:
        print(f)
        x = x + 1
else:
    print(f)
    print(f)
    f2 = 1
    x = 1
    while x < repeat:
        f3 = f + f2
        print(f3)
        f = f2
        f2 = f3
        x = x + 1
