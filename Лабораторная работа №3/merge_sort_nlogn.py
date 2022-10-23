"""Сортировка слиянием - O(nlogn)"""
from random import randint


def merge_sort(nums):
    if len(nums) > 1:
        middle = len(nums) // 2
        left_part = nums[:middle]
        right_part = nums[middle:]
        merge_sort(left_part)
        merge_sort(right_part)

        i = j = k = 0
        while i < len(left_part) and j < len(right_part):
            if left_part[i] < right_part[j]:
                nums[k] = left_part[i]
                i += 1
            else:
                nums[k] = right_part[j]
                j += 1
            k += 1

        while i < len(left_part):
            nums[k] = left_part[i]
            i += 1
            k += 1

        while j < len(right_part):
            nums[k] = right_part[j]
            j += 1
            k += 1


array = [randint(1, 100) for i in range(20)]
print(array)
merge_sort(array)
print(array)
