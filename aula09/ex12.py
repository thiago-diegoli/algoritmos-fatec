matriz = [[float(input(f'Digite um elemento (coluna {i+1}, linha {n+1}): ')) for n in range(3)] for i in range(3)]
matriz_transposta = [[0,0,0] for i in range(3)]
for i in matriz:
    for n in i:
        a = matriz.index(i)
        b = i.index(n)
        matriz_transposta[b][a] = matriz[a][b]
print(f'Matriz transposta:\n{matriz_transposta}')
