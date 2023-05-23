vetor = [int(input(f'Digite o {i+1}o. número: ')) for i in range(10)]
vetor.reverse()
print('Ordem inversa: ')
[print(i, end=' ') for i in vetor]