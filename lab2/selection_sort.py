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
