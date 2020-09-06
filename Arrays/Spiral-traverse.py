"""SPIRAL TRAVERSE -Write a function that takes in an n x m two-dimensional array (that can be square-shaped when n == m) and returns a one-dimensional array of all the array's elements in spiral order. Spiral order starts at the top left corner of the two-dimensional array, goes to the right, and proceeds in a spiral pattern all the way until every element has been visited."""

# ITERATIVE SOLUTION
# array is nxm matrix
# O(N+M)T | O(N+M)S


def spiralTraverse(array):
    res = []
    # Tackles n rows
    startRow, endRow = 0, len(array)-1
    # Tackles n columns
    startCol, endCol = 0, len(array[0])-1
    while startRow <= endRow and startCol <= endCol:
        for i in range(startCol, endCol+1):
            res.append(array[startRow][i])
        for i in range(startRow+1, endRow+1):
            res.append(array[i][endCol])
        for i in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            res.append(array[endRow][i])
        for i in reversed(range(startRow+1, endRow)):
            if startCol == endCol:
                break
            res.append(array[i][startCol])
        startCol += 1
        endCol -= 1
        startRow += 1
        endRow -= 1
    return res
