salario = int (input('Seu salario atual: '))
porcentagem = int (input('Porcentagem de aumento: '))
porcentagem = porcentagem / 100
print(f'Seu salario atual é: {salario + (salario * porcentagem)}')
