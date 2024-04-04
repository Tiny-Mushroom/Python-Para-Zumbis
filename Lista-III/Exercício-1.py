while True:
    nota = int (input("digite o valor da nota. "))
    if 0 <= nota <= 10:
        print('Nota registrada')
        print('Sua nota é: ', nota)
        break
    else:
        print('Nota inválida!')