print("Digite os numeros do MAIOR para o MENOR.")
a = int (input("Digite o comprimento do primeiro lado: "))
b = int (input("Digite o comprimento do segundo lado: "))
c = int (input("Digite o comprimento terceiro lado: "))

if (a + b) > c and (a + c) > b and (b + c) > a and a == b == c:
    print("Este triângulo é eequilatero.")
elif (a + b) > c and (a + c) > b and (b + c) > a and a == b != c:
    print("Este triângulo é isóceles.")
elif (a + b) > c and (a + c) > b and (b + c) > a and a > b > c:
    print("este triangulo é escaleno.")
else:
    print("Estes lados não formam um triângulo.")