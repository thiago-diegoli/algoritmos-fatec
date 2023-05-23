from numpy import dot
matriz = [[int(input(f'Digite um elemento (coluna {i+1}, linha {n+1}): ')) for n in range(10)] for i in range(20)]
vetor = []
for i in range(len(matriz[0])):  
    soma = 0
    for n in range(len(matriz)):
        soma += matriz[n][i]
    vetor.append([soma])
print(f'A matriz multiplicada pelo vetor com as somas das linha:\n{[dot(matriz,vetor)]}')