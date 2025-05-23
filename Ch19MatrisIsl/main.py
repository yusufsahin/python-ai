A = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print(A[0][0])
print(A[0][1])
print(A[2][2])

B=[[9, 8, 7],[6, 5, 4],[3, 2, 1]]

def add_matrices(A, B):
    return  [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def sub_matrices(A, B):
    return  [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
print(add_matrices(A, B))
print(sub_matrices(A, B))

def matrix_mul(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

C = [[1, 2], [3, 4]]
D = [[2, 0], [1, 2]]
# Çarpım: [[4, 4], [10, 8]]

print(matrix_mul(C, D))