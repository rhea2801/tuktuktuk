"""Min Number Of Jumps - You're given a non-empty array of positive integers where each integer represents the maximum number of steps you can take forward in the array. For example, if the element at index 1 is 3 , you can go from index 1 to index 2 , 3 , or 4 . Write a function that returns the minimum number of jumps needed to reach the final index. Note that jumping from index i to index i + x always constitutes one jump, no matter how large x is."""

# O(N^2) T | O(N) S


def minNumberOfJumps(array):
	jumps = [float("inf") for x in array]
	jumps[0] = 0
	for i in range(len(array)):
		for j in range(0, i):
			if array[j] + j >= i:
				jumps[i] = min(jumps[j] + 1, jumps[i])
	return jumps[-1]


# METHOD 2
# O(N)T | O(1)S
def minNumberOfJumps(array):
	if len(array) == 1:
		return 0
	jumps = 0
    maxReach = array[0]
	steps = array[0]
	for i in range(1,len(array)-1):
		maxReach = max(maxReach, array[i]+i)
		steps-=1
		if steps == 0:
			jumps += 1
			steps = maxReach - i
	return jumps+1
