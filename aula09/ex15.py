matriz = [[float(input(f'Digite um elemento (coluna {i+1}, linha {n+1}): ')) for n in range(8)] for i in range(8)]
simetria = 0
for i in matriz:
    for n in i:
        a = matriz.index(i)
        b = i.index(n)
        if matriz[a][b] == matriz[b][a]:
            simetria += 1
if simetria == len(matriz)*len(matriz[0]):
    print('A matriz digitada é simétrica')
else:
    print('A matriz digitada não é simétrica')