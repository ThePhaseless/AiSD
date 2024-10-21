from lab1.insertion_sort import insertion_sort


def lazarus_sort(tab: list[int]):
    swaps = 0
    k = 1
    while (gap := 2*(len(tab)//(2**k))) > 0:
        k += 1
        if (gap == 1):
            swaps += insertion_sort(tab)
            break
        for i in range(0, len(tab)-gap):
            j = i+gap
            if (tab[i] > tab[j]):
                swaps += 1
                tab[i], tab[j] = tab[j], tab[i]
    return swaps
