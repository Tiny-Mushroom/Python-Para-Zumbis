tempoD = int (input('Digite o tempo em Dias: '))
tempoH = int (input('Digite o tempo em horas: '))
tempoM = int (input('Digite o tempo em minutos: '))
tempoS = int (input('Digite o tempo em segundo: '))
tempoD = tempoD * 86400
tempoH = tempoH * 3600
tempoM = tempoM * 60
print(f'tempo total em segundos: {tempoD + tempoH + tempoM + tempoS}')