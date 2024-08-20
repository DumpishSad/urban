def get_matrix(n, m, value):
    matrix = []
    for i in range(0, n):
        matrix.append([])
        for j in range(0, m):
            matrix[i].append(value)
    return matrix

matrix_=get_matrix(3, 5, 42)
print(matrix_)
