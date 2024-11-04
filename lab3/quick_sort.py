def quick_sort(tab: list[int]) -> list[int]:
    if len(tab) <= 1:
        return tab

    pivot = tab[0]
    less = [x for x in tab[1:] if x <= pivot]
    greater = [x for x in tab[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)
