matriz = [[int(input(f'Digite um elemento (coluna {i+1}, linha {n+1}): ')) for n in range(2)] for i in range(2)]
maior = 0
for i in matriz:
    for n in i:
        if n > maior:
            maior = n
print(f'O maior elemento da matriz é {maior}')
matriz_mult = []
for i in matriz:
    matriz_mult.append([n*maior for n in i])
print(f'Matriz multiplicada por {maior}:\n{matriz_mult}')
