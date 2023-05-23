preco = float(input('Digite o valor da compra: '))
if preco <= 1000:
    desconto = 10
elif preco <= 5000:
    desconto = 20
else:
    desconto = 30
print(f'Você recebeu {desconto}% de desconto')
print(f'O valor total da compra será R$ {preco*(1-desconto/100):.2f}')
