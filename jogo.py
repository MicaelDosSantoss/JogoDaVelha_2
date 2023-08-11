from escolha import Escolha_do_usuario, rival

lista = [1,2,3,4,5,6,7,8,9]

while True: 

    print(f' {lista[0]} | {lista[1]} | {lista[2]} \n {lista[3]} | {lista[4]} | {lista[5]} \n {lista[6]} | {lista[7]} | {lista[8]} \n')

    ladoEscohido = int(input('\nEscoloha um número disponível acima: '))

    for i in lista:
        ladoEscohido-1
        if ladoEscohido == i:
            lista[i] = Escolha_do_usuario