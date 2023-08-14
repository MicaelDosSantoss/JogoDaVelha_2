
def vencedor(escolhido,rival,lista):

    li = []
    for i in lista:
        li.append(i)

   
    if li[0] == escolhido and li[4] == escolhido and li[8] == escolhido:
        r = f"\n Vencedor {escolhido}\n"
        return r
        