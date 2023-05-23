from funcoes import rolar_dado
on = True
score_c, score_j = 0, 0
while on:
    jogador = rolar_dado()
    print(f'\nVocê rolou o dado e obteve um {jogador}')
    computador = rolar_dado()
    print(f'Você rolou o dado e obteve um {computador}')
    if computador == jogador:
        print('Empate')
        score_c += 0.5
        score_j += 0.5
    elif computador > jogador:
        print('Você perdeu!')
        score_c += 1
    else:
        print('Você venceu!')
        score_j += 1
    while True:
        continuar = input('Deseja jogar novamente? (S ou N) ')
        if continuar.strip().upper() in ['S','N']:
            if continuar.strip().upper() == 'N':
                on = False
                print(f'\nPlacar final: {score_j} x {score_c}\n')
            break
        else: print('Resposta inválida')