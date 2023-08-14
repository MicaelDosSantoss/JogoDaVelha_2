
def vencedor(escolhido,rival,lista):

    li = []
    for i in lista:
        li.append(i)

# Diagonal
    if li[0] == escolhido and li[4] == escolhido and li[8] == escolhido:
        r = f"\n Vencedor {escolhido}\n"
        return r

    if li[0] == rival and li[4] == rival and li[8] == rival:
        r = f"\n Vencedor {rival}\n"
        return r  
    
    if li[2] == escolhido and li[4] == escolhido and li[6] == escolhido:
        r = f"\n Vencedor {escolhido}\n"
        return r
    
    if li[2] == rival and li[4] == rival and li[6] == rival:
        r = f"\n Vencedor {rival}\n"
        return r
    
# Coluna    
    if li[0] == escolhido and li[3] == escolhido and li[6] == escolhido:
        r = f"\n Vencedor {escolhido}\n"
        return r
    
    if li[0] == rival and li[3] == rival and li[6] == rival:
        r = f"\n Vencedor {rival}\n"
        return r
    
    if li[1] == escolhido and li[4] == escolhido and li[7] == escolhido:
        r = f"\n Vencedor {escolhido}\n"
        return r
    
    if li[1] == rival and li[4] == rival and li[7] == rival:
        r = f"\n Vencedor {rival}\n"
        return r
    
    if li[2] == escolhido and li[5] == escolhido and li[8] == escolhido:
        r = f"\n Vencedor {escolhido}\n"
        return r
    
    if li[2] == rival and li[5] == rival and li[8] == rival:
        r = f"\n Vencedor {rival}\n"
        return r
# linha

    if li[0] == escolhido and li[1] == escolhido and li[2] == escolhido:
        r = f"\n Vencedor {escolhido}\n"
        return r
    
    if li[0] == rival and li[1] == rival and li[2] == rival:
        r = f"\n Vencedor {rival}\n"
        return r
    
    if li[3] == escolhido and li[4] == escolhido and li[5] == escolhido:
        r = f"\n Vencedor {escolhido}\n"
        return r
    
    if li[3] == rival and li[4] == rival and li[5] == rival:
        r = f"\n Vencedor {rival}\n"
        return r
    
    if li[6] == escolhido and li[7] == escolhido and li[8] == escolhido:
        r = f"\n Vencedor {escolhido}\n"
        return r
    
    if li[6] == rival and li[7] == rival and li[8] == rival:
        r = f"\n Vencedor {rival}\n"
        return r
    
    if isinstance(li[0], str) and isinstance(li[1], str) and isinstance(li[2], str) and isinstance(li[3], str) and isinstance(li[4], str) and isinstance(li[5], str) and isinstance(li[6], str) and isinstance(li[7], str) and isinstance(li[8], str):
        r = f"\n Empate!"
        return r
    
