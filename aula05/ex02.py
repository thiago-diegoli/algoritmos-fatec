n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3
print(f'A media das notas é {media:.1f}')
if media < 3:
    print('Reprovado')
elif media < 7:
    print('Exame')
    print(f'A nota mínima necessária para aprovação deve ser {12-media}')
else:
    print('Aprovado')
