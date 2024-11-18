from typing import Callable

from lab3.faster_quick_sort import faster_quick_sort
from lab3.merge_sort import merge_sort
from lab3.quick_sort import quick_sort
from lab4.heap_sort import heap_sort
from lib import random_array, test_algorithm


print("Input tab length: ")
n = None
while not n:
    try:
        n = int(input())
    except ValueError:
        print("Wrong input")

algorithms_available: list[Callable[[list[int]], int | list[int]]] = [
    merge_sort,
    heap_sort,
    quick_sort,
    faster_quick_sort,
]

print("\n")
tab_og = random_array(n)

tab_sorted = tab_og.copy()
tab_sorted.sort()

for algorithm in algorithms_available:
    tab = tab_og.copy()
    print(f"Algorithm: {algorithm.__name__}")
    tab_new = test_algorithm(algorithm, tab)
    if isinstance(tab_new, list):
        tab = tab_new
    if tab != tab_sorted:
        raise Exception("Algorithm did not sort correctly")
