frase = input('Digite uma frase: ')
vogal = 0
for i in frase:
    if i in 'aeiou':
        vogal += 1
print(f'Há {vogal} vogal(is) nessa frase')