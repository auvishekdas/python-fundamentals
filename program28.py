matrix = [
    [14,42,85,96,99],
    [13,9,94,95,33],
]
print(matrix[1][3])

matrix = [
    [12,14,15,18,20],
    [13,9,31,32,34],
    
]
matrix[0][2] = 25
print(matrix[0][2])

matrix = [
    [25,48,78],
    [78,48,25],

]
for row in matrix:
    for col in row:
        print(col)
