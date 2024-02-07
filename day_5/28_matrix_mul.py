x = [
    [12, 7, 3],  # i x j
    [4, 5, 6],
    [7, 8, 9],
]
y = [
    [5, 8, 1, 2],  # j x k
    [6, 7, 3, 0],
    [4, 5, 9, 1],
]

row_x = len(x)
col_x = len(x[0])
row_y = len(y)
col_y = len(y[0])

xy = [[0 for k in range(col_y)] for i in range(row_x)]  # i x k
if col_x != row_y:
    print("Cannot be multiplied")
    exit()

for i in range(row_x):
    for k in range(col_y):
        for j in range(row_y):
            xy[i][k] += x[i][j] * y[j][k]

print(xy)
