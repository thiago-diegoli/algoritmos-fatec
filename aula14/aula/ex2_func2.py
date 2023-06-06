from ex2_func1 import sera_primo
def quantos_primos(n):
    primos = 0
    for i in range(n):
        if sera_primo(i):
            primos += 1
    return primos

