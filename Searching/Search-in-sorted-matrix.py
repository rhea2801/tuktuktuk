"""Search In Sorted Matrix - You're given a two-dimensional array (a matrix) of distinct integers and a target integer. Each row in the matrix is sorted, and each column is also sorted; the matrix doesn't necessarily have the same height and width. Write a function that returns an array of the row and column indices of the target integer if it's contained in the matrix, otherwise [-1, -1]"""

# O(N+M) T | O(1) S


def searchInSortedMatrix(matrix, target):
    row = 0
    column = len(matrix[0])-1
    while row < len(matrix) and column >= 0:
        if(matrix[row][column]) > target:
            column -= 1
        elif(matrix[row][column]) < target:
            row += 1
        else:
            return [row, column]

    return [-1, -1]
