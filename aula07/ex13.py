# Exercício 3 utilizando while
media_peso, media_altura = 0, 0
imc = []
while len(imc) != 20:
    peso = float(input('Digite um peso (em kg): '))
    altura = float(input('Digite uma altura (em metros): '))
    media_peso += peso
    media_altura += altura
    imc.append(peso/altura**2)
print(f'A media de peso é {media_peso/20:.1f} Kg')
print(f'A media de altura é {media_altura/20:.2f} metros')
print(f'O maior e menor IMC são respectivamente: {max(imc):.1f} e {min(imc):.1f}')
