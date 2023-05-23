idade = int(input('Digite sua idade: '))
if idade >= 5:
    if idade < 8:
        categoria = 'Infantil'
    elif idade < 11:
        categoria = 'Juvenil'
    elif idade < 16:
        categoria = 'Adolescente'
    elif idade < 31:
        categoria = 'Adulto'
    else:
        categoria = 'Sênior'
    print(f'Você pertence a categoria {categoria}')
else:
    print('Você não pertence a nenhuma categoria')
