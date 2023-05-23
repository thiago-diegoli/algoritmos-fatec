matriz = [[float(input(f'Digite um elemento (coluna {i+1}, linha {n+1}): ')) for n in range(4)] for i in range(4)]
soma = 0
for i in range(4):
    soma += matriz[i][i]
print(f'A soma da diagonal principal da matriz é {soma:.1f}')
