idades = []
while True:
    idade = int(input('Digite uma idade: '))
    if idade == 0:
        break
    idades.append(idade)
print(f'Foram digitadas {len(idades)} idades')
print(f'A media das idades equivale a {sum(idades)/len(idades):.1f}')