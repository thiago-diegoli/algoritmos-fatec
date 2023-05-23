n = int(input('Digite um número: '))
positivo_negativo = 'positivo'
impar_par = 'par'
if n % 2:
    impar_par = 'impar'
if n < 0:
    positivo_negativo = 'negativo'
print(f'O número {n} é {impar_par} e {positivo_negativo}')
        