class Heap:
    def __init__(self, child):
        self.Heap = []
        self.child = child

    def __swap(self, i, j):
        self.Heap[i], self.Heap[j] = self.Heap[j], self.Heap[i]

    def __move_up(self, index):
        parent_index = (index - 1) // self.child
        if index > 0 and self.Heap[parent_index] < self.Heap[index]:
            self.__swap(parent_index, index)
            self.__move_up(parent_index)

    def __move_down(self, index):
        largest = index
        first_child_index = index * self.child + 1
        possible_child_indexes = [first_child_index + i
                                  for i in range(self.child)]
        child_indexes = [i for i in possible_child_indexes
                         if i < len(self.Heap)]

        for child_index in child_indexes:
            if self.Heap[child_index] > self.Heap[largest]:
                largest = child_index

        if largest != index:
            self.__swap(index, largest)
            self.__move_down(largest)

    def return_max(self):
        if len(self.Heap) > 1:
            self.__swap(0, len(self.Heap) - 1)
            maximum = self.Heap.pop()
            self.__move_down(0)
        elif self.Heap:
            maximum = self.Heap.pop()
        else:
            return "Heap is empty"
        return maximum

    def add_value(self, value):
        self.Heap.append(value)
        self.__move_up(len(self.Heap) - 1)

    def print_heap_by_row(self):
        old_val = 0
        cur_val = 1
        i = 0
        while True:
            if cur_val >= len(self.Heap):
                print(f'Row{i+1}: {self.Heap[old_val:len(self.Heap)]}')
                break
            else:
                print(f'Row{i+1}: {self.Heap[old_val:cur_val]}')
            old_val += self.child**i
            cur_val = old_val + self.child**(i+1)
            i += 1
