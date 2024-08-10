def gauss_elimination(A, b):
    n = len(A)

    # Elimination phase
    for i in range(n):
        # Partial pivoting
        max_row = i
        for k in range(i+1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        # Zeroing out below the pivot
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # Back substitution
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i] / A[i][i]
        for j in range(i):
            b[j] -= A[j][i] * x[i]

    return x

# Example usage
A = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]

b = [8, -11, -3]

solution = gauss_elimination(A, b)
formatted_solution = [round(sol, 1) for sol in solution]
print("Solution:", formatted_solution)
