from matplotlib import pyplot as plt
from heap import Heap
import time

two_heap = Heap(2)
five_heap = Heap(5)
seven_heap = Heap(7)
ex = Heap(2)
two_y = []
five_y = []
seven_y = []
with open("number_file", "r") as f:
    number_list = [int(number) for number in f.read().split(", ")]
x_axis = []
for i in range(0, 100001, 10000):
    x_axis.append(i)
    two_heap = Heap(2)
    five_heap = Heap(5)
    seven_heap = Heap(7)
    start_time = time.time()
    for number in number_list[:i]:
        two_heap.add_value(number)
    two_y.append(time.time()-start_time)

    for number in number_list[:i]:
        five_heap.add_value(number)
    five_y.append(time.time()-start_time)

    for number in number_list[:i]:
        seven_heap.add_value(number)
    seven_y.append(time.time()-start_time)

plt.plot(x_axis, two_y, label="two-heap")
plt.plot(x_axis, five_y, label="five-heap")
plt.plot(x_axis, seven_y, label="seven-heap")
plt.xlabel("Ilość elementow dodanych")
plt.ylabel("Czas dodawania (s)")
plt.title("Porównanie czasów dodawania do ilości słów")
plt.legend()
plt.grid(True)
plt.savefig("./graphs/graphex.png")
plt.clf()

two_y = []
five_y = []
seven_y = []


x_axis = []
for i in range(0, 100001, 10000):
    x_axis.append(i)
    two_heap = Heap(2)
    five_heap = Heap(5)
    seven_heap = Heap(7)
    for number in number_list:
        two_heap.add_value(number)
        five_heap.add_value(number)
        seven_heap.add_value(number)
    start_time = time.time()
    for j in range(i):
        two_heap.return_max()
    two_y.append(time.time()-start_time)

    for j in range(i):
        five_heap.return_max()
    five_y.append(time.time()-start_time)

    for j in range(i):
        seven_heap.return_max()
    seven_y.append(time.time()-start_time)

plt.plot(x_axis, two_y, label="two-heap")
plt.plot(x_axis, five_y, label="five-heap")
plt.plot(x_axis, seven_y, label="seven-heap")
plt.xlabel("Ilość elementow dodanych")
plt.ylabel("Czas dodawania (s)")
plt.title("Porównanie czasów zwrotu max do ilości słów")
plt.legend()
plt.grid(True)
plt.savefig("./graphs/graphex2.png")
plt.clf()
