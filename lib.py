from copy import deepcopy
from typing import Callable


def check(tab: list[int], sorter: Callable[[list[int]], int]):
    new_tab = deepcopy(tab)
    print(sorter(new_tab))
    print(new_tab)
