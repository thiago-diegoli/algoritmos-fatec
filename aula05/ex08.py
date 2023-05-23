preco = int(input('Digite o preço líquido do produto: '))
codigo = int(input('Digite o código de origem do produto: '))
if codigo == 1:
    procedencia = 'Sul'
    imposto = 11
elif codigo == 2:
    procedencia = 'Norte'
    imposto = 13
elif codigo == 3:
    procedencia = 'Nordeste'
    imposto = 9
elif codigo == 4:
    procedencia = 'Centro-Oeste'
    imposto = 12
elif codigo == 5:
    procedencia = 'Sudeste'
    imposto = 18
else:
    print('Código inválido')
    codigo = 0
if codigo:
    print(f'Procedência: {procedencia}')
    print(f'Preço final: R$ {preco*(imposto/100+1):.2f}')
