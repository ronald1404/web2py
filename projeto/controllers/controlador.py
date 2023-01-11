def acao():
    print ('_'*80)
    lista1.append("controlador inseriu na lista 1")
    print(lista1)
    del lista2 [1]
    print("controlador removeu item da lista 2")
    print (lista2)
    print ("acao irá se comunicar com visão")
    return dict(lista1=lista1, lista2=lista2,meses=meses)
