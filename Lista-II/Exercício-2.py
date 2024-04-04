def isleap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

year = int (input("Digite o ano: "))

leapYear = isleap(year)

if leapYear:
    print("É ano bisexto.")
else:
    print("Não é ano bisexto")