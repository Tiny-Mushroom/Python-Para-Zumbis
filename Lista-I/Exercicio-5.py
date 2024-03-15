preco = int (input('preço da mercadoria: '))
porcentagem = int (input('Porcentagem de desconto: '))
porcentagem = porcentagem / 100
print(f'O preço da mercadoria com desconto é: {preco - (preco * porcentagem)}')