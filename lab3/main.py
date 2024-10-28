

from lab1 import insertion_sort


def quick_sort(tab: list[int]) -> list[int]:
    if len(tab) <= 1:
        return tab

    pivot = tab[0]
    less = [x for x in tab[1:] if x <= pivot]
    greater = [x for x in tab[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)


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


def faster_quick_sort(tab: list[int]) -> list[int]:
    if len(tab) <= 10:
        return insertion_sort.insertion_sort(tab)

    if len(tab) <= 1:
        return tab

    pivot = tab[0]
    less = [x for x in tab[1:] if x <= pivot]
    greater = [x for x in tab[1:] if x > pivot]

    return faster_quick_sort(less) + [pivot] + faster_quick_sort(greater)


tab = [1, 5, 6, 2, 4, 3]
print(quick_sort(tab.copy()))
print(merge_sort(tab.copy()))
