def insertion_sort(lista):
    lista = list(lista)
    out_list = [lista[0]]
    for i in range(1, len(lista)):
        first_word = out_list[-1]
        second_word = lista[i]
        if first_word > second_word:
            for index, word in enumerate(reversed(out_list)):
                if second_word > word:
                    out_list.insert(len(out_list)-index, second_word)
                    break
                if index == len(out_list)-1:
                    out_list.insert(0, second_word)
        else:
            out_list.append(second_word)
    return out_list
