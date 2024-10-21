from lab1.insertion_sort import insertion_sort


def shell_sort(tab: list[int]):
    swaps = 0
    gap = len(tab)
    while (gap := gap//2) > 0:
        gap = gap//2
        if (gap == 1):
            swaps += insertion_sort(tab)
            break
        for i in range(0, len(tab)-gap):
            j = i+gap
            if (tab[i] > tab[j]):
                swaps += 1
                tab[i], tab[j] = tab[j], tab[i]
    return swaps
