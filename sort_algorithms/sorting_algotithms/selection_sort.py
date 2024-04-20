def selection_sort(lista):
    lista = list(lista)
    out_list = [None]*len(lista)
    for i in range(len(lista)):
        minimum = min(lista)
        lista.remove(minimum)
        out_list[i] = minimum
    return out_list
