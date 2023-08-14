from escolha import rival
from random import choice

def contra(lista):
    lista_c = []

    for i in lista:
        if isinstance(i, int):
            lista_c.append(i)

    if len(lista_c) == 0:
        r = 'parar'
        return r
    else:           
        r = choice(lista_c)
        return r

       
    