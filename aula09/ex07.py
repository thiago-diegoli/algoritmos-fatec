primos = []
contador = 101
while len(primos) != 10:
    primo = True
    for i in range(2, contador):
        if contador % i == 0:
            primo = False
    if primo:
        primos.append(contador)
    contador += 1
print('10 primeiros primos acima de 100: ')
[print(i) for i in primos]