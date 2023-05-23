salario = float(input('Digite seu salário: '))
aumento = float(input('Digite o aumento (%): '))/100+1
print(f'Seu novo salário será {salario*aumento:.2f}')