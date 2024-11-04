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

algorithms_available: list[Callable[[list[int]], int | list[int] | None]] = [
    merge_sort,
    heap_sort,
    quick_sort,
    faster_quick_sort,
]

print("\n")
tab = random_array(n)
for algorithm in algorithms_available:
    print(f"Algorithm: {algorithm.__name__}")
    test_algorithm(algorithm, tab)
