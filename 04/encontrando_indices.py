def encontre_indices(lista, item):
    lista_de_indices = []
    for indice, value in enumerate(lista):
        if value == item:
            lista_de_indices.append([indice])
        elif isinstance(lista[indice], list):
            for i in encontre_indices(lista[indice], item):
                lista_de_indices.append([indice] + i)
    return lista_de_indices