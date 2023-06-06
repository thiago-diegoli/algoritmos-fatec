from ex2_func1 import sera_primo
from ex2_func2 import quantos_primos
primos = []
i = 0
# Input do usuário
n = 35*2+5
while len(primos) != quantos_primos(n):
    i += 1
    if sera_primo(i):
        primos.append(i)
print(f'Os números primos até {n}: {primos}')
print(f'A soma de todos os primos até {n} é {sum(primos)}')

