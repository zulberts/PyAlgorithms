import random
import time
import matplotlib.pyplot as plt
from BST import BST


def generate_data(size, upper_limit):
    return [random.randint(1, upper_limit) for _ in range(size)]


def test_bst_operations(data, steps):
    insert_times = []
    search_times = []
    delete_times = []

    for n in steps:
        subset = data[:n]
        bst = BST()

        start_time = time.time()
        for value in subset:
            bst.insert(value)
        insert_times.append(time.time() - start_time)

        start_time = time.time()
        for value in subset:
            bst.search(value)
        search_times.append(time.time() - start_time)

        start_time = time.time()
        for value in subset:
            bst.delete(value)
        delete_times.append(time.time() - start_time)

    return insert_times, search_times, delete_times


def main():
    data_size = 10000
    steps = list(range(1000, 10001, 1000))
    data = generate_data(data_size, 30000)
    insert_times, search_times, delete_times = test_bst_operations(data, steps)

    plt.figure(figsize=(10, 5))
    plt.plot(steps, insert_times, label="Insertion Times", marker="o")
    plt.title("BST Insertion Time")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.savefig("bst_insertion_time.jpg")
    plt.clf()

    plt.figure(figsize=(10, 5))
    plt.plot(steps, search_times, label="Search Times", marker="o")
    plt.title("BST Search Time")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.savefig("bst_search_time.jpg")
    plt.clf()

    plt.figure(figsize=(10, 5))
    plt.plot(steps, delete_times, label="Deletion Times", marker="o")
    plt.title("BST Deletion Time")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.savefig("bst_deletion_time.jpg")


if __name__ == "__main__":
    main()
