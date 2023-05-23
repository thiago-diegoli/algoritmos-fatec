idades = {input('Digite o sobrenome: '):int(input('Digite a idade: ')) for i in range(10)}
print(f'O sobrenome com mais idade é: {max(idades, key=idades.get)}')

