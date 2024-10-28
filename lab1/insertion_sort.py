def insertion_sort(tab: list[int]):
    swaps = 0
    for i in range(1, len(tab)):
        k = tab[i]
        j = i - 1
        while j >= 0 and tab[j] > k:
            tab[j + 1] = tab[j]
            j -= 1
        swaps += 1
        tab[j + 1] = k
    return tab
