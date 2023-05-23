ano_nasc = int(input('Digite o ano que nasceu: '))
ano_atual = int(input('Digite o ano atual: '))
idade = ano_atual - ano_nasc
print(f"""Você possui aproximadamente:
{idade} anos ou
{idade*12} meses ou
{idade*365} dias ou
{idade*365/7:.0f} semanas.""")