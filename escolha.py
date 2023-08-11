

rival = ''

while True:

    Escolha_do_usuario = input('Você pode escolhe o X ou O: ')

    if Escolha_do_usuario == 'X' or Escolha_do_usuario == 'x':
        rival = 'O'
        print(f'`Você escolheu {Escolha_do_usuario}, rival escolheu {rival}')
        break

    if Escolha_do_usuario == 'O' or Escolha_do_usuario == 'o':
        rival = 'X'
        print(f'`Você escolheu {Escolha_do_usuario}, rival escolheu {rival}')
        break

    else:
        print('Digite novamente!')