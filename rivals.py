from escolha import rival
from random import choice

def contra(lista):
    lista_c = []

    for i in lista:
        if isinstance(i, int):
            lista_c.append(i)
            
    r = choice(lista_c)
    return r    
            
            
    
  