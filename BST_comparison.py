import random
import time
import matplotlib.pyplot as plt
from BST import BST


def generate_numbers(n, max_val):
    return [random.randint(1, max_val) for _ in range(n)]


def measure_insertion(tree, numbers):
    start = time.time()
    for number in numbers:
        tree.insert(number)
    return time.time() - start


def measure_search(tree, numbers):
    start = time.time()
    for number in numbers:
        tree.search(number)
    return time.time() - start


def measure_deletion(tree, numbers):
    start = time.time()
    for number in numbers:
        tree.delete(number)
    return time.time() - start


def main():
    n_values = [1000, 2000, 5000, 10000]
    max_val = 30000
    all_numbers = generate_numbers(max_val, 30000)

    insertion_times = []
    search_times = []
    deletion_times = []

    for n in n_values:
        bst = BST()
        numbers = all_numbers[:n]

        insertion_time = measure_insertion(bst, numbers)
        insertion_times.append(insertion_time)

        search_time = measure_search(bst, numbers)
        search_times.append(search_time)

        deletion_time = measure_deletion(bst, numbers)
        deletion_times.append(deletion_time)

    plt.figure(figsize=(12, 6))
    plt.plot(n_values, insertion_times, label="Insertion Times")
    plt.plot(n_values, search_times, label="Search Times")
    plt.plot(n_values, deletion_times, label="Deletion Times")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.title("BST Performance")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
