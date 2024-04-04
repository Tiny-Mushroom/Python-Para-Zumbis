area = float (input("Qual o tamanho da area a ser pintada? "))
volume = int (round(area / 3))
latas = int (round(volume / 18))
preco = latas * 80.00
print(f"Você deverá comprar {latas} latas. O preço total será de R${preco}.2f")
