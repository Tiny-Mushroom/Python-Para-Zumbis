excesso = 0
multa = 0

peso = float (input("Digite o peso do peixe em quilos: "))

if peso > 50:
    excesso = peso - 50
    multa = excesso * 4.00

print(f'Excesso: {excesso}kg. Multa: R${multa}')