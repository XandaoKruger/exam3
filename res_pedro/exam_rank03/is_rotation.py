def is_rotation(arr1: list, arr2: list) -> bool:
    return sorted(arr1) == sorted(arr2)


print(is_rotation([1, 2, 3, 4, 5], [4, 5, 1, 2, 3]))
print(is_rotation([1, 2, 3, 4, 5], [5, 1, 2, 3, 4]))
print(is_rotation([1, 2, 3], [3, 2, 1]))
print(is_rotation([1, 2], [1, 2, 3]))
print(is_rotation([], []))
