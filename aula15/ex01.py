atletas = []
while True:
    nome = input('Digite o nome do atleta: ')
    if nome == '':
        break
    print('')
    distancias = []
    vez = {0:'Primeiro',1:'Segundo',2:'Terceiro',3:'Quarto',4:'Quinto'}
    for i in range(5):
        dist = float(input(f'{vez[i]} salto: '))
        distancias.append(dist)
    print('')
    atleta = [nome, distancias]
    atletas.append(atleta)
if atletas != []:
    print('\nResultado final')
    for i in atletas:
        print(f'Atleta: {i[0]}')
        print(f'Saltos: {i[1][0]} - {i[1][1]} - {i[1][2]} - {i[1][3]} - {i[1][4]}')
        print(f'Media do saltos: {(sum(i[1])/5):.2f}\n')
