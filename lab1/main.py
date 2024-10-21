

from lab1.hibbard_sort import hibbard_sort
from lab1.insertion_sort import insertion_sort
from lab1.lazarus_sort import lazarus_sort
from lab1.shell_sort import shell_sort


tablica = [5, 2, 4, 6, 1, 3]
print(tablica)

print("Insertion:")
insertion_tab = tablica.copy()
print(insertion_sort(insertion_tab))
print(insertion_tab)

print("Shell:")
shell_tab = tablica.copy()
print(shell_sort(shell_tab))
print(shell_tab)

print("Lazarus:")
lazarus_tab = tablica.copy()
print(lazarus_sort(lazarus_tab))
print(lazarus_tab)

print("Hibbard:")
hibbard_tab = tablica.copy()
print(hibbard_sort(hibbard_tab))
print(hibbard_tab)
