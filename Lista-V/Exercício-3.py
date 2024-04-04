cnt = 0

for i in range(1067, 3627):
    if i % 2 == 0 and i % 7 == 0:
        cnt = cnt + 1

print('Numeros pares divisiveis por 7 entre 1067 e 3627:', cnt)
