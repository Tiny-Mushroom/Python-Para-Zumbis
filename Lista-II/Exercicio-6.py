salario = float (input('Quanto você ganha por hora? '))
tempo = int (input('Quantas horas você trabalha por mes? '))
bruto = salario * tempo
imposto = bruto * (11 / 100)
inss = bruto * (8 / 100)
sindicato = bruto * (5 / 100)
liquido = bruto - imposto - inss - sindicato

print('+ Salário bruto: R$', bruto)
print('- IR(11%):  R$', imposto)
print('- INSS(8%): R$', inss)
print('- Sindicato(5%); R$', sindicato)
print('= Salário Líquido: R$', liquido)
