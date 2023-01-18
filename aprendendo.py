import os 
# A lista
lista = []

#Funções:
def adicionar(lista):
    while True:
        nova_add = input('Adicione os novos objetos:')
        if nova_add == '':
            print('Sua lista não pode estar vazia!')
            continue
        if nova_add == 'sair':
            break
        else:
            os.system('cls')
            lista.append(nova_add)
            print('Sua lista:')
            listar(lista)
def remover(lista):
    os.system('cls')
    listar(lista)
    remover = input(f'Selecione uma das opções acima para remover: ')
    indice = int(remover)
    del lista[indice]
    listar(lista)
def listar(lista):
    for i, valor in enumerate(lista):
        print(i, valor) 
#O loop
while True:
    os.system('cls')
    if lista == []:
        print('Sua lista está vazia!')
    else:
        print('Sua lista:')
    listar(lista)
    print('Escolha uma das opções abaixo!')
    op =  input('(A)dicionar (R)emover').capitalize()
    if op == 'A' or 'R': 
        ...
    else:
        print('Selecione uma das opções válidas!')
    if op == 'A':
        os.system('cls')
        adicionar(lista)
    elif op == 'R':
        remover(lista)
    else:
        print('Selecione uma das opções válidas!')
#Fim do loop
