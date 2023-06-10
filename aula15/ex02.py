enquete = []
while True:
    try:
        voto = int(input("""Qual o melhor Sistema Operacional para uso em servidores?
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
"""))
    except:
        print('Valor inválido!')
        continue
    if voto not in [0,1,2,3,4,5,6]:
        print('Valor inválido!')
        continue
    if voto == 0:
        break
    enquete.append(voto)
t = len(enquete)
if t:
    print('Sistema Operacional\tVotos\t %')
    print(f'{"-"*20}\t{"-"*7}\t {"-"*3}')
    sos = ['Windows Server','Unix','Linux','Netware','Mac OS','Outro']
    maior = 0
    for i in sos:
        votos_so = enquete.count(sos.index(i)+1)
        print(f'{i:20}\t{votos_so}\t {(100*(votos_so/t)):2.1f}%')
        if votos_so > maior:
            maior = votos_so
            so = i
            frequencia = 100*(votos_so/t)
    print(f'{"-"*20}\t{"-"*7}\t {"-"*3}')
    print(f'{"Total":20}\t{len(enquete)}')
    print(f'\nO Sistema Operacional mais votado foi o {so}, com {maior} voto(s), correspondendo a {frequencia}% dos votos.')
else:
    print('Nenhum voto')
