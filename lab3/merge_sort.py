def merge_sort(tab: list[int]) -> list[int]:
    if (len(tab) <= 1):
        return tab

    middle = len(tab) // 2

    left = merge_sort(tab[:middle])
    right = merge_sort(tab[middle:])
    i, j = 0, 0
    sorted: list[int] = []
    while i in range(len(left)) and j in range(len(right)):
        if left[i] < right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1

    sorted += left[i:]
    sorted += right[j:]
    return sorted
