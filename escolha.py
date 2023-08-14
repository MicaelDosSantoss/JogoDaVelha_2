color_green = "\033[1;32m"
color_blue = "\033[1;34m"
close_color = "\033[m"

rival = ''

while True:

    Escolha_do_usuario = input('Você pode escolhe o X ou O: ')

    if Escolha_do_usuario == 'X' or Escolha_do_usuario == 'x':
        Escolha_do_usuario = f"{color_green}X{close_color}"
        rival = f'{color_blue}O{close_color}'
        print(f'`Você escolheu {Escolha_do_usuario}, rival escolheu {rival}')
        break

    if Escolha_do_usuario == 'O' or Escolha_do_usuario == 'o':
        Escolha_do_usuario = f"{color_green}O{close_color}"
        rival = f'{color_blue}X{close_color}'
        print(f'`Você escolheu {Escolha_do_usuario}, rival escolheu {rival}')
        break

    else:
        print('Digite novamente!')