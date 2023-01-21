import os
lista_cp = []
# funtions
def listar(lista_cp):
    for i, valor in enumerate(lista_cp):
        print(i, valor)
def adicionar(lista_cp):
    valor = input('Nova adição: ')
    lista_cp.append(valor)
def remover(lista_cp):
    remover = input('Escolha uma opção para remover: ')
    indice = int(remover)
    del lista_cp[indice]
# loop
while True:
    print('Selecione uma opção')
    op = input('[r]emover [l]istar [a]dicionar ')
    if op == 'r':
        os.system('cls')
        print('Remover')
        remover(lista_cp)
    elif op == 'l':
        os.system('cls')
        print('Listar')
        listar(lista_cp)
        if list == 0:
            print('Nada para listar')
    elif op == 'a':
        os.system('cls')
        print('Adicionar')
        adicionar(lista_cp)
    else:
        print('Escolha uma opção válida!')









