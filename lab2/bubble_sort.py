def bubble_sort(tab: list[int]) -> int:
    swaps = 0
    for j in range(0, len(tab)-1):
        if tab[j] > tab[j+1]:
            tab[j], tab[j+1] = tab[j+1], tab[j]
            swaps += 1
    if swaps == 0:
        return swaps
    return bubble_sort(tab=tab) + swaps
