maior, linha, coluna = 0, 0, 0
matriz = [[int(input(f'Digite um elemento (coluna {i+1}, linha {n+1}): ')) for n in range(10)] for i in range(10)]
for i in matriz:
    for n in i:
        if n > maior:
            maior = n
            linha = matriz.index(i)+1
            coluna = i.index(n)+1
print(f'O maior número é {maior} e está localizado na linha {linha} e coluna {coluna}')
