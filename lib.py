from random import randint
import time
from typing import Callable


def random_array(tab_length: int) -> list[int]:
    return [randint(-100, 100) for _ in range(tab_length)]


def test_algorithm(sorter: Callable[[list[int]], int | list[int] | None], tab_length: int = 10,):
    tab = random_array(tab_length)
    tab_og = tab.copy()
    start_time = time.time_ns()
    sorter(tab)
    end_time = time.time_ns()
    print("Original tab: ", tab_og)
    print("Sorted tab: ", tab)
    print(f"Sort time: {end_time - start_time} ns")
    if isinstance(tab, int):
        print("Swaps: ", tab)
    print('\n')
