from random import randint
import time
from typing import Callable


def random_array(tab_length: int) -> list[int]:
    return [randint(-100, 100) for _ in range(tab_length)]


def test_algorithm(sorter: Callable[[list[int]], int | list[int]], tab: list[int]):
    start_time = time.time_ns()
    sorter(tab)
    end_time = time.time_ns()
    print("Sorted tab: ", tab)
    print(f"Sort time: {end_time - start_time} ns")
    if isinstance(tab, int):
        print("Swaps: ", tab)
    else:
        yield tab
    print('\n')
