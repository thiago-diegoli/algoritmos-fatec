def pato_coelho(patas, cabecas):
    coelhos = 0
    while True:
        patos = cabecas - coelhos
        if patos*2 + coelhos*4 >= patas:
            return {'Coelhos':coelhos, 'Patos':patos}
        elif coelhos > cabecas:
            return 'Valores inválido'
        coelhos += 1
print(pato_coelho(38*3+1,38))