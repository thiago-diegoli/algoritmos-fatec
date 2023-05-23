n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
escolha = int(input("""Digite um número para escolher:
1 - Média
2 - Diferença
3 - Multiplicação
4 - Divisão
"""))
if escolha == 1:
    print(f'A media dos números digitados equivale a {(n1+n2)/2:.1f}')
elif escolha == 2:
    print(f'A diferença do menor para o maior equivale a {max(n1,n2)-min(n1,n2):.1f}')
elif escolha == 3:
    print(f'O produto dos números digitados equivale a {n1*n2:.1f}')
elif escolha == 4:
    print(f'A divisão do primeiro pelo segundo número equivale a {n1/n2:.1f}')
else:
    print('Número inválido')
