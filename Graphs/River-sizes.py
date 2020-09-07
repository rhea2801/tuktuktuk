"""River Sizes - You're given a two-dimensional array (a matrix) of potentially unequal height and width containing only e s and 1 s. Each e represents land, and each 1 represents part of a river. A river consists of any number of 1 s that are either horizontally or vertically adjacent (but not diagonally adjacent). The number of adjacent 1 s forming a river determine its size. Note that a river can twist. In other words, it doesn't have to be a straight vertical line or a straight horizontal line; it can be L-shaped, for example. Write a function that returns an array of the sizes of all rivers represented in the input matrix. The sizes don't need to be in any particular order."""

# O(N) T | O(N) S


def riverSizes(matrix):
    sizes = []
    visited = [[False for value in row] for row in matrix]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNodes(i, j, matrix, visited, sizes)
    return sizes


def traverseNodes(i, j, matrix, visited, sizes):
    currRiverSize = 0
    nodesToExplore = [[i, j]]
    while len(nodesToExplore):
        currNode = nodesToExplore.pop()
        i = currNode[0]
        j = currNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currRiverSize += 1
        unvisitedNeighbors = getUnvisitedNeighbors(matrix, i, j, visited)
        for neighbor in unvisitedNeighbors:
            nodesToExplore.append(neighbor)
    if currRiverSize > 0:
        sizes.append(currRiverSize)


def getUnvisitedNeighbors(matrix, i, j, visited):
    unvisitedNeighbors = []

    if(i > 0 and not visited[i-1][j]):
        unvisitedNeighbors.append([i-1, j])

    if(i < len(matrix)-1 and not visited[i+1][j]):
        unvisitedNeighbors.append([i+1, j])

    if(j > 0 and not visited[i][j-1]):
        unvisitedNeighbors.append([i, j-1])

    if(j < len(matrix[0])-1 and not visited[i][j+1]):
        unvisitedNeighbors.append([i, j+1])

    return unvisitedNeighbors
