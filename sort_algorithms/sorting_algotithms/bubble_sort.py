def bubble_sort(lista):
    lista = list(lista)
    while True:
        swap_no = 0
        for i in range(len(lista)-1):
            first_word = lista[i]
            second_word = lista[i+1]
            if first_word > second_word:
                lista[i+1] = first_word
                lista[i] = second_word
                swap_no += 1
        if not swap_no:
            return lista
