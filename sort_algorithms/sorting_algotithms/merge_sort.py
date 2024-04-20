def merge_sort(words):
    if len(words) <= 1:
        return words
    middle_word = len(words) // 2
    left_words = merge_sort(words[:middle_word])
    right_words = merge_sort(words[middle_word:])
    return merge(left_words, right_words)


def merge(left_words, right_words):
    sorted_list = [None] * (len(left_words) + len(right_words))
    left_track = right_track = sorted_track = 0
    while left_track < len(left_words) and right_track < len(right_words):
        if left_words[left_track] < right_words[right_track]:
            sorted_list[sorted_track] = left_words[left_track]
            left_track += 1
        else:
            sorted_list[sorted_track] = right_words[right_track]
            right_track += 1
        sorted_track += 1
    while left_track < len(left_words):
        sorted_list[sorted_track] = left_words[left_track]
        left_track += 1
        sorted_track += 1
    while right_track < len(right_words):
        sorted_list[sorted_track] = right_words[right_track]
        right_track += 1
        sorted_track += 1
    return sorted_list
