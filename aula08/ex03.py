while True:
    n = list(str(int(input('Digite um número com 9 dígitos: '))))
    if len(n) != 9:
        print('Não possui 9 digitos')
    else:
        break    
n.insert(1,'.')
n.insert(5,'.')
n.insert(-2,',')
print(''.join(n))