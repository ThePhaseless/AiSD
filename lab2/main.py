
from lib import check


def bubble_sort(tab: list[int]) -> int:
    swaps = 0
    for j in range(0, len(tab)-1):
        if tab[j] > tab[j+1]:
            tab[j], tab[j+1] = tab[j+1], tab[j]
            swaps += 1
    if swaps == 0:
        return swaps
    return bubble_sort(tab=tab) + swaps


def selection_sort(tab: list[int]) -> int:
    swaps = 0
    for j in range(0, len(tab)-1):
        min = j
        for i in range(j+1, len(tab)):
            if tab[i] < tab[min]:
                min = i
        if min != j:
            tab[j], tab[min] = tab[min], tab[j]
            swaps += 1
    return swaps


tab = [5, 2, 4, 6, 1, 3]
check(tab=tab, sorter=bubble_sort)
check(tab=tab, sorter=selection_sort)
