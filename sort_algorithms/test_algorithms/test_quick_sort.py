from sorting_algorithms.quick_sort import quick_sort


def test_sorted_numbers():
    lista = [1, 2, 3, 4, 5]
    assert quick_sort(lista) == sorted(lista)


def test_unsorted_numbers():
    lista = [3, 1, 2, 5, 4]
    assert quick_sort(lista) == sorted(lista)


def test_unsorted_numbers_2():
    lista = [5, 4, 3, 2, 1]
    assert quick_sort(lista) == sorted(lista)


def test_sorted_words():
    lista = ["adam", "bartek", "cezary", "damian", "eryk"]
    assert quick_sort(lista) == sorted(lista)


def test_unsorted_words():
    lista = ["cezary", "adam", "bartek", "eryk", "damian"]
    assert quick_sort(lista) == sorted(lista)


def test_sorted_words_numbers():
    lista = ["1", "2", "3", "adam", "bartek"]
    assert quick_sort(lista) == sorted(lista)


def test_unsorted_words_numbers():
    lista = ["bartek", "2", "1", "3", "adam"]
    assert quick_sort(lista) == sorted(lista)
