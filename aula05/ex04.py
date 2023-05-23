altura = float(input('Digite sua altura (em metros): '))
sexo = input('Digite o seu sexo (M ou F): ')
if sexo.upper() == 'M':
    peso = 72.7*altura-58
else:
    peso = 62.1*altura-44.7
print(f'Seu peso ideal equivale a {peso:.1f} kg')
