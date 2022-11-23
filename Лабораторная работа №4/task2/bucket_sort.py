def bucket_sort(array):
    if len(array) <= 1:
        return array

    max_value = max(array)
    min_value = min(array)

    if min_value == max_value:
        return array

    length = len(array)
    size = float(max_value - min_value) / length

    buckets = [[] for _ in range(length)]

    for i in range(length):
        index = int((array[i] - min_value) / size)
        if index != length:
            buckets[index].append(array[i])
        else:
            buckets[index - 1].append(array[i])

    for i in range(len(array)):
        buckets[i] = bucket_sort(buckets[i])

    result = []
    for i in range(length):
        result = result + buckets[i]

    return result


array = [int(i) for i in input("Введите список чисел через пробел: ").split()]
sorted_array = bucket_sort(array)
print(f"Отсортированный список: {sorted_array}")
