cnt = 0

for i in range(18644, 33088):
    if 2 in str(i) and 7 not in str(i):
        cnt = cnt + 1

print('Quantidade de números sortudos:', cnt)