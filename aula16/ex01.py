def sobrenome_func():
    while True:
        sobrenome = input('Digite o sobrenome: ')
        if sobrenome:
            if sobrenome.isalpha():
                return sobrenome
            else:
                print('Digite um sobrenome válido!')
        else:
            return sobrenome
        
def idade_func():
    while True:
        try: 
            idade = int(input('Digite a idade: '))
        except:
            print('Digite uma idade válida!')
            continue
        else:
            return idade

def altura_func():
    while True:
        try: 
            altura = int(input('Digite a altura (em cm): '))
        except:
            print('Digite uma altura válida!')
            continue
        else:
            return altura

def peso_func():
    while True:
        try: 
            peso = float(input('Digite o peso (em kg): '))
        except:
            print('Digite uma peso válida!')
            continue
        else:
            return peso
pessoas = []
while True:
    sobrenome = sobrenome_func()
    if sobrenome == '':
        break
    idade = idade_func()
    altura = altura_func()
    peso = peso_func()
    pessoa = [sobrenome, idade, altura, peso]
    pessoas.append(pessoa)
if pessoas != []:
    pessoas.sort()
    n = 0
    total_i, total_a, total_p = 0, 0, 0
    for i in pessoas:
        n += 1
        print('-'*50)
        print(f'Pessoa {n}: ')
        print('Sobrenome\tIdade\tAltura\tPeso')
        print(f'{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}')
        total_i += i[1]
        total_a += i[2]
        total_p += i[3]
    print('-'*50)
    total = len(pessoas)
    print(f"Idade média: {total_i/total}")
    print(f"Altura média: {total_a/total}")
    print(f"Peso médio: {total_p/total}")
    print('-'*50)