n = int (input('Digite um numero inteiro positivo. '))
if n % 42 == 0:
    print('Resposta para tudo')
elif n % 3 == 0 and n % 5 == 0:
    print('Fizzbuzz')
elif n % 5 == 0:
    print('Buzz')
elif n % 3 == 0:
    print('Fizz')
else:
    print(n)