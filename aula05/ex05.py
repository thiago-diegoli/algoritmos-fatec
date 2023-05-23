ano = int(input('Digite o ano que nasceu: '))
idade = 2023 - ano
print(f'Você possui {idade} anos')
if idade >= 16:
    print('Você possui idade para poder votar')
if idade >= 18:
    print('Você possui idade para conseguir a carteira de habilitação')