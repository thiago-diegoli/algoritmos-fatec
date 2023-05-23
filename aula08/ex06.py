texto = input('Digite algo: ').replace(' ','').upper()
if texto != texto[::-1]:
    print('O que você digitou não é um palíndromo')
else:
    print('Você digitou um palíndromo')