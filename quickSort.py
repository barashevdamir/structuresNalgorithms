# Быстрая сортировка (quickSort) — это один из наиболее известных и широко применяемых алгоритмов сортировки.
# Она основана на использовании стратегии "разделяй и властвуй".
# В этом коде мы выбираем элемент в середине списка в качестве "опорного".
# Затем мы создаем три списка: один для элементов меньше опорного, один для элементов равных опорному, и один для элементов больше опорного.
# Мы рекурсивно применяем быструю сортировку к списку элементов, которые меньше и больше опорного элемента.
# Это продолжается до тех пор, пока не останется список, который нужно сортировать. В конце, мы объединяем отсортированные списки вместе.

def quickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quickSort(left) + middle + quickSort(right)

# Тестирование
arr = [3,4,7,11,12,1,12,5,6,7]
print(quickSort(arr))
