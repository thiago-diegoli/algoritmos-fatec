palavras = []
while len(palavras) != 20:
    palavra = input(f'Escreva uma palavra (max. 10 caracteres): ')
    if len(palavra) > 10:
        print('Passou de 10 caracteres')
    else:
        palavras.append(palavra)
palavras = [print(i[::-1]) for i in palavras]
