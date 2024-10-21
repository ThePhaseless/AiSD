def hibbard_sort(tab: list[int]):
    swaps = 0
    k = 1
    while (gap := 2**k-1) > 0:
        k += 1
        for i in range(0, len(tab)-gap):
            j = i+gap
            if (tab[i] > tab[j]):
                swaps += 1
                tab[i], tab[j] = tab[j], tab[i]
    return swaps
