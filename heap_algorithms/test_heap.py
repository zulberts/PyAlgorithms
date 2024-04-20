from heap import Heap


def test_init_with_2():
    heap = Heap(2)
    assert heap.child == 2


def test_init_with_3():
    heap = Heap(3)
    assert heap.child == 3


def test_init_with_7():
    heap = Heap(7)
    assert heap.child == 7


def test_return_max_empty_heap():
    heap = Heap(2)
    assert heap.return_max() == "Heap is empty"


def test_return_max_single_element():
    heap = Heap(2)
    heap.add_value(10)
    assert heap.return_max() == 10


def test_return_max_multiple_elements():
    heap = Heap(2)
    for i in [1, 3, 2]:
        heap.add_value(i)
    assert heap.return_max() == 3


def test_return_max_repeated_calls():
    heap = Heap(2)
    for i in [5, 3, 8]:
        heap.add_value(i)
    heap.return_max()
    assert heap.return_max() == 5


def test_return_max_after_adding_more_elements():
    heap = Heap(2)
    for i in [4, 6, 8]:
        heap.add_value(i)
    heap.return_max()
    heap.add_value(7)
    assert heap.return_max() == 7


def test_add_value_and_check_heap_property():
    heap = Heap(2)
    for i in [3, 2, 1]:
        heap.add_value(i)
    assert heap.Heap[0] >= max(heap.Heap[1:])


def test_add_value_check_length():
    heap = Heap(2)
    for i in range(5):
        heap.add_value(i)
    assert len(heap.Heap) == 5


def test_add_value_check_order_after_multiple_operations():
    heap = Heap(2)
    for i in [5, 3, 8, 6]:
        heap.add_value(i)
    heap.return_max()
    assert heap.Heap[0] >= max(heap.Heap[1:])


def test_add_value_negative():
    heap = Heap(2)
    heap.add_value(-1)
    assert heap.Heap[0] == -1


def test_add_value_zero():
    heap = Heap(2)
    heap.add_value(0)
    assert heap.Heap[0] == 0


def test_print_heap_empty(capsys):
    heap = Heap(2)
    heap.print_heap_by_row()
    captured = capsys.readouterr()
    assert captured.out == "Row1: []\n"


def test_print_heap_single_element(capsys):
    heap = Heap(2)
    heap.add_value(1)
    heap.print_heap_by_row()
    captured = capsys.readouterr()
    assert "Row1: [1]" in captured.out


def test_print_heap_multiple_elements(capsys):
    heap = Heap(2)
    for i in [3, 2, 1]:
        heap.add_value(i)
    heap.print_heap_by_row()
    captured = capsys.readouterr()
    assert "Row1: " in captured.out and "Row2: " in captured.out


def test_print_heap_full_binary_tree(capsys):
    heap = Heap(2)
    for i in range(1, 8):
        heap.add_value(i)
    heap.print_heap_by_row()
    captured = capsys.readouterr()
    assert "Row3: " in captured.out


def test_print_heap_with_different_child_factors(capsys):
    heap = Heap(3)
    for i in range(1, 10):
        heap.add_value(i)
    heap.print_heap_by_row()
    captured = capsys.readouterr()
    assert "Row2: " in captured.out and "Row3: " in captured.out
