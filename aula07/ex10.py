while True:
    base = int(input('Digite a base: '))
    altura = int(input('Digite a altura: '))
    if 0 in [base, altura]:
        print('Medidas inválidas, não pode haver 0')
    else:
        break
print(f'A área do triângulo equivale a {base*altura/2:.1f}')
