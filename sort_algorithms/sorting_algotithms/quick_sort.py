def quick_sort(words):
    if len(words) <= 1:
        return words
    else:
        pivot = words[len(words) // 2]
        left = [word for word in words if word < pivot]
        middle = [word for word in words if word == pivot]
        right = [word for word in words if word > pivot]
        return quick_sort(left) + middle + quick_sort(right)
