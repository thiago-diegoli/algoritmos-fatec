frase = input('Digite uma frase: ')
palavra = input('Digite uma palavra:')
contador = 0
for i in frase.split():
    if i == palavra:
        contador += 1
print(f'A palavra {palavra} aparece {contador} vez(es) na frase')