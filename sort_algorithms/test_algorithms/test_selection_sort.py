from sorting_algorithms.selection_sort import selection_sort


def test_sorted_numbers():
    lista = [1, 2, 3, 4, 5]
    assert selection_sort(lista) == sorted(lista)


def test_unsorted_numbers():
    lista = [3, 1, 2, 5, 4]
    assert selection_sort(lista) == sorted(lista)


def test_unsorted_numbers_2():
    lista = [5, 4, 3, 2, 1]
    assert selection_sort(lista) == sorted(lista)


def test_sorted_words():
    lista = ["adam", "bartek", "cezary", "damian", "eryk"]
    assert selection_sort(lista) == sorted(lista)


def test_unsorted_words():
    lista = ["cezary", "adam", "bartek", "eryk", "damian"]
    assert selection_sort(lista) == sorted(lista)


def test_sorted_words_numbers():
    lista = ["1", "2", "3", "adam", "bartek"]
    assert selection_sort(lista) == sorted(lista)


def test_unsorted_words_numbers():
    lista = ["bartek", "2", "1", "3", "adam"]
    assert selection_sort(lista) == sorted(lista)
