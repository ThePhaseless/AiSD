from lab1 import insertion_sort


def faster_quick_sort(tab: list[int]) -> list[int]:
    if len(tab) <= 10:
        insertion_sort.insertion_sort(tab)
        return tab

    if len(tab) <= 1:
        return tab

    pivot = tab[0]
    less = [x for x in tab[1:] if x <= pivot]
    greater = [x for x in tab[1:] if x > pivot]

    return faster_quick_sort(less) + [pivot] + faster_quick_sort(greater)
