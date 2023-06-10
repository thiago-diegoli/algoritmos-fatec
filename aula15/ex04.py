def verificar_ip(ip):
    end_ip = ip.split('.')
    end_ip = [int(i) for i in end_ip]
    if len(end_ip) != 4:
        return False
    for i in end_ip:
        if i > 255 or i < 0:
            return False
    return True

arquivo = open('aula15/ex04_entrada.txt','r')
corretos, incorretos = [], []
for i in arquivo:
    if verificar_ip(i):
        corretos.append(i)
    else:
        incorretos.append(i)
arquivo.close()


saida = open('aula15/ex04_saida.txt', 'w', encoding='utf-8')

saida.write('[Endereços válidos:]\n')
for i in corretos:
    saida.write(i)

saida.write('\n[Endereços inválidos:]\n')
for i in incorretos:
    saida.write(i)
saida.close()
