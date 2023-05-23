deposito = float(input('Digite o valor do deposito: '))
juros = float(input('Digite o valor da taxa de juros: '))/100
rendimento = deposito*juros
print(f'Valor do rendimento: {rendimento:.2f}')
print(f'Valor total após rendimento: {rendimento+deposito:.2f}')