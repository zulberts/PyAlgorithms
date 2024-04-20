from heap import Heap


def print_heaps():
    for child in [2, 3, 7]:
        print(f"\nCreating a {child}-ary heap...")
        heap = Heap(child)
        for i in range(1, 50):
            heap.add_value(i)
        heap.print_heap_by_row()


if __name__ == "__main__":
    print_heaps()
