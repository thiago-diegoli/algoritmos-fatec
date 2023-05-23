vetor = [int(input(f'Digite o {i+1}o. número: ')) for i in range(10)]
print(f'O maior valor digitado foi {max(vetor)} na posição {vetor.index(max(vetor))}')