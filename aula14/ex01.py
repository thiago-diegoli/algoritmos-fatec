arquivo = open('aula14/usuarios.txt','r')
nomes, numeros = [], []
for i in arquivo:
    linha = i.split()
    nomes.append(linha[0])
    numeros.append(int(linha[1]))
arquivo.close()
relatorio = open('aula14/relatorio.txt', 'w', encoding='utf-8')
relatorio.writelines(['ACME Inc. \t Uso do espaço em disco pelos usuários\n', f'{"-"*45}\n'])
relatorio.write('Nr.\tUsuário \t Espaço utilizado \t % do uso\n')
contador = 0
total = sum(numeros)/1024/1024/100
for i in nomes:
    contador += 1
    espaco = numeros[contador-1]/1024/1024
    relatorio.writelines([f'{contador}\t', f'{i:10}', f'{espaco:12.2f} MB', f'{(espaco/total):15.2f}%\n'])
relatorio.write(f'\nEspaço total ocupado: {(total*100):.2f} MB\n')
relatorio.write(f'Espaço total ocupado: {(total*100/len(numeros)):.2f} MB')
relatorio.close()