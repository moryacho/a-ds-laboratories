def heap_sort(array):
    build_max_heap(array)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        max_local_heap(array, 0, i)


def build_max_heap(array):
    length = len(array)
    start = (length - 2) // 2
    while start >= 0:
        max_local_heap(array, start, length)
        start = start - 1


def max_local_heap(array, parent_ind, size):
    l = 2 * parent_ind + 1
    r = 2 * parent_ind + 2
    if l < size and array[l] > array[parent_ind]:
        largest_ind = l
    else:
        largest_ind = parent_ind
    if r < size and array[r] > array[largest_ind]:
        largest_ind = r
    if largest_ind != parent_ind:
        array[largest_ind], array[parent_ind] = array[parent_ind], array[largest_ind]
        max_local_heap(array, largest_ind, size)


array = [int(i) for i in input("Введите список чисел через пробел: ").split()]
heap_sort(array)
print(f"Отсортированный список: {array}")
