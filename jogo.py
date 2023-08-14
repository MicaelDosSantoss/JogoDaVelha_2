from escolha import Escolha_do_usuario, rival
from rivals import contra
from vencer import vencedor

# print("\033[1;31mTexto em vermelho\033[m")
# print("\033[1;32mTexto em verde\033[m")
# print("\033[1;34mTexto em azul\033[m")

color_red = "\033[1;31m"
color_green = "\033[1;32m"
color_blue = "\033[1;34m"
close_color = "\033[m"

c = 0

lista = [0,1,2,3,4,5,6,7,8]

while True:
    
    valid = False 

    jogo = print(f' {lista[0]} | {lista[1]} | {lista[2]} \n {lista[3]} | {lista[4]} | {lista[5]} \n {lista[6]} | {lista[7]} | {lista[8]} \n')
    ladoEscolhido = int(input('\nEscolha um número disponível acima: \n'))

    for i in range(len(lista)):
        
        if isinstance(lista[i], int) and 0 <= ladoEscolhido <= 8:
            if ladoEscolhido == lista[i]:
                lista[i] = f'{Escolha_do_usuario}'
                valid = True

    

    riv = contra(lista)
    print(riv)

    for i in range(len(lista)):
        if riv == lista[i]:
            lista[i] = f'{rival}'             
                 
    if not valid:
        print(f'\n{color_red}RESULTADO INVALIDO{close_color}\n')
    
    vencer = vencedor(Escolha_do_usuario,rival,lista)

    if isinstance(vencer,str):
        print(f'\n{color_green}{vencer}{close_color}')
        break
    