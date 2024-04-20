from sorting_algorithms.bubble_sort import bubble_sort
from sorting_algorithms.insertion_sort import insertion_sort
from sorting_algorithms.selection_sort import selection_sort
from sorting_algorithms.merge_sort import merge_sort
from sorting_algorithms.quick_sort import quick_sort
import time
from matplotlib import pyplot as plt
import sys


def format_file(file):
    file = open(file, "r").read().split("\n")
    outfile = []
    for line in file:
        outfile += (line.strip().split(" "))
    return outfile


x_axis = []
bubble_y = []
selection_y = []
insertion_y = []
merge_sort_y = []
quick_sort_y = []


for j in range(1, 5):
    sys.setrecursionlimit(j * 1000)
    x_axis.clear()
    bubble_y.clear()
    selection_y.clear()
    insertion_y.clear()
    merge_sort_y.clear()
    quick_sort_y.clear()
    for i in range(100, (j * 1000) + 1, 100):
        x_axis.append(i)
        file = format_file("pan-tadeusz.txt")[:i]
        start_time = time.time()
        bubble_sort(file)
        bubble_y.append(time.time()-start_time)
        start_time = time.time()
        selection_sort(file)
        selection_y.append(time.time()-start_time)
        start_time = time.time()
        insertion_sort(file)
        insertion_y.append(time.time()-start_time)
        start_time = time.time()
        merge_sort(file)
        merge_sort_y.append(time.time()-start_time)
        start_time = time.time()
        quick_sort(file)
        quick_sort_y.append(time.time()-start_time)
    plt.plot(x_axis, bubble_y, label="bubble sort")
    plt.plot(x_axis, selection_y, label="selection sort")
    plt.plot(x_axis, insertion_y, label="insertion sort")
    plt.plot(x_axis, merge_sort_y, label='merge sort')
    plt.plot(x_axis, quick_sort_y, label='quick sort')
    plt.xlabel("Ilość słów posortowanych")
    plt.ylabel("Czas sortowania (s)")
    plt.title(f"Porównanie czasów sortowania do ilości słów {j * 1000}")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"./graphs/graph{j * 1000}.png")
    plt.clf()


for j in range(10, 11):
    sys.setrecursionlimit(j * 1000)
    x_axis.clear()
    bubble_y.clear()
    selection_y.clear()
    insertion_y.clear()
    merge_sort_y.clear()
    quick_sort_y.clear()
    for i in range(500, (j * 1000) + 1, 500):
        x_axis.append(i)
        file = format_file("pan-tadeusz.txt")[:i]
        start_time = time.time()
        bubble_sort(file)
        bubble_y.append(time.time() - start_time)
        start_time = time.time()
        selection_sort(file)
        selection_y.append(time.time() - start_time)
        start_time = time.time()
        insertion_sort(file)
        insertion_y.append(time.time() - start_time)
        start_time = time.time()
        merge_sort(file)
        merge_sort_y.append(time.time() - start_time)
        start_time = time.time()
        quick_sort(file)
        quick_sort_y.append(time.time() - start_time)
    plt.plot(x_axis, bubble_y, label="bubble sort")
    plt.plot(x_axis, selection_y, label="selection sort")
    plt.plot(x_axis, insertion_y, label="insertion sort")
    plt.plot(x_axis, merge_sort_y, label="merge sort")
    plt.plot(x_axis, quick_sort_y, label="quick sort")
    plt.xlabel("Ilość słów posortowanych")
    plt.ylabel("Czas sortowania (s)")
    plt.title(f"Porównanie czasów sortowania do ilości słów {j * 1000}")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"./graphs/graph{j * 1000}.png")
    plt.clf()


for j in range(30, 45, 5):
    sys.setrecursionlimit(j * 1000)
    x_axis.clear()
    bubble_y.clear()
    selection_y.clear()
    insertion_y.clear()
    merge_sort_y.clear()
    quick_sort_y.clear()
    for i in range(500, (j * 1000) + 1, 500):
        x_axis.append(i)
        file = format_file("pan-tadeusz.txt")[:i]
        start_time = time.time()
        merge_sort(file)
        merge_sort_y.append(time.time() - start_time)
        start_time = time.time()
        quick_sort(file)
        quick_sort_y.append(time.time() - start_time)
    plt.plot(x_axis, merge_sort_y, label="merge sort")
    plt.plot(x_axis, quick_sort_y, label="quick sort")
    plt.xlabel("Ilość słów posortowanych")
    plt.ylabel("Czas sortowania (s)")
    plt.title(f"Porównanie czasów sortowania do ilości słów {j * 1000}")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"./graphs/graph_quick_merge_comparison{j * 1000}.png")
    plt.clf()


for j in range(1, 5):
    x_axis.clear()
    bubble_y.clear()
    selection_y.clear()
    insertion_y.clear()
    merge_sort_y.clear()
    quick_sort_y.clear()
    for i in range(10, (j * 1000) + 1, 10):
        x_axis.append(i)
        file = format_file("pan-tadeusz.txt")[:i]
        file = sorted(file)
        start_time = time.time()
        bubble_sort(file)
        bubble_y.append(time.time() - start_time)
        start_time = time.time()
        selection_sort(file)
        selection_y.append(time.time() - start_time)
        start_time = time.time()
        insertion_sort(file)
        insertion_y.append(time.time() - start_time)
        start_time = time.time()
        merge_sort(file)
        merge_sort_y.append(time.time() - start_time)
        start_time = time.time()
        quick_sort(file)
        quick_sort_y.append(time.time() - start_time)
    plt.plot(x_axis, bubble_y, label="bubble sort")
    plt.plot(x_axis, selection_y, label="selection sort")
    plt.plot(x_axis, insertion_y, label="insertion sort")
    plt.plot(x_axis, merge_sort_y, label="merge sort")
    plt.plot(x_axis, quick_sort_y, label="quick sort")
    plt.xlabel("Ilość słów posortowanych")
    plt.ylabel("Czas sortowania (s)")
    plt.title(f"Porównanie czasów sortowania do ilości słów {j * 1000}")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"./graphs/graph_sorted{j * 1000}.png")
    plt.clf()
