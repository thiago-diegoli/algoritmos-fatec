from time import sleep
m = 10
s = 0
print('Contagem regressiva de 10 minutos')
while True:
    print(f'{m:02d}:{s:02d}')
    if s == 0:
        m -= 1
        s = 59
    else:
        s -= 1
    if s == 0 and m == 0:
        break
    sleep(1)
print('Fim')