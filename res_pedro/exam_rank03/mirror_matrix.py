def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    res: list[list[int]] = []
    for i in matrix:
        res += [i[::-1]]
    return res


print(mirror_matrix([[1, 2, 3], [4, 5, 6]]))
print(mirror_matrix([[1, 2], [3, 4], [5, 6]]))
print(mirror_matrix([[7]]))
print(mirror_matrix([[1, 2, 3, 4]]))
print(mirror_matrix([[-1, -2], [-3, -4]]))
