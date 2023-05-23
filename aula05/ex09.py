x = float(input('Digite o primeiro lado do triângulo: '))
y = float(input('Digite o segundo lado do triângulo: '))
z = float(input('Digite o terceiro lado do triângulo: '))
if x > y + z or y > x + z or z > x + y:
    print('Não forma um triângulo')
else:
    if x == y and y == z:
        print('Triângulo Equilátero')
    elif x == y or y == z or z == x:
        print('Triângulo Isósceles')
    else:
        print('Triângulo Escaleno')