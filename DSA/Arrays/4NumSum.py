"""FOUR NUMBER SUM - Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. The function should find all quadruplets in the array that sum up to the target sum and return a two-dimensional array of all these quadruplets in no particular order. If no four numbers sum up to the target sum, the function should return an empty array."""

# O(N^2) T on average | O(N^3) T | O(N^2) S


def fourNumberSum(array, targetSum):
	quadruplets = []
	allPairsSums = {}
	for i in range(1, len(array)-1):
		for j in range(i+1, len(array)):
			currentSum = array[i] + array[j]
			difference = targetSum - currentSum
			if (difference in allPairsSums):
				for pair in allPairsSums[difference]:
					quadruplets.append(pair+[array[i], array[j]])
		for k in range(0, i):
			currentSum = array[i]+array[k]
			if currentSum not in allPairsSums:
				allPairsSums[currentSum] = [[array[i], array[k]]
			else:
				allPairsSums[currentSum].append([array[i], array[k]])
	return quadruplets
