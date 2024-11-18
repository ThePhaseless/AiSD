def heapify(tab: list[int], n: int, i: int):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and tab[l] > tab[largest]:
        largest = l
    if r < n and tab[r] > tab[largest]:
        largest = r
    if largest != i:
        tab[i], tab[largest] = tab[largest], tab[i]
        heapify(tab, n, largest)


def heap_sort(tab: list[int]):
    n = len(tab)
    for i in range(n // 2 - 1, -1, -1):
        heapify(tab, n, i)
    for i in range(n - 1, 0, -1):
        tab[0], tab[i] = tab[i], tab[0]
        heapify(tab, i, 0)
    return tab
