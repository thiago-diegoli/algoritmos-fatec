combustivel = input("""Escolha qual tipo de combustível deseja:
G - Gasolina
D - Diesel
A - Álcool
""")
litros = int(input('Digite quantos litros deseja: '))
if combustivel.upper() == 'G':
    valor = 2.1009
elif combustivel.upper() == 'D':
    valor = 0.9798
elif combustivel.upper() == 'A':
    valor = 1.7997
print(f'O valor total a pagar será R$ {valor*litros:.2f}')