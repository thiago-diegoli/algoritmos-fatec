vetor1 = [int(input(f'Digite o {i+1}o. número: ')) for i in range(10)]
vetor2 = [int(input(f'Digite o {i+1}o. número: ')) for i in range(10)]
vetor3 = []
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])
print(f'Lista intercalada: {vetor3}')
