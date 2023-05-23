s = float(input('Digite o valor do salário mínimo: '))/8
qwatt = int(input('Digite a quantidade de quilowatts de uma residência: '))
print(f"""Cada quilowatt custa R$ {s:.2f}
A residência deve pagar R$ {s*qwatt:.2f}
Valor com desconto de 15%: R$ {s*qwatt*0.85:.2f}""")