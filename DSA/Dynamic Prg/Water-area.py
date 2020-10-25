"""Water Area - You're given an array of non-negative integers where each non-zero integer represents the height of a pillar of width 1 . Imagine water being poured over all of the pillars; write a function that returns the surface area of the water trapped between the pillars viewed from the front. Note that spilled water should be ignored. Refer to the first minute of this question's video explanation for a visual example."""

#O(N) T | O(1) S

def waterArea(heights):
	water = 0	
	tallestRight = [0 for x in heights]
	maxHtRight = 0	
	tallestLeft = [0 for x in heights]
	maxHtLeft = 0	
	
	for i in reversed(range(len(tallestRight))):
		tallestRight[i] = maxHtRight
		maxHtRight = max(maxHtRight, heights[i])
		
	for i in range(len(tallestLeft)):
		tallestLeft[i] = max(maxHtLeft, heights[i])
		maxHtLeft = max(maxHtLeft,heights[i])
		
	for i in range(len(heights)):			
		leftMax = tallestLeft[i]
		rightMax = tallestRight[i]		
		minHeight = min(leftMax, rightMax)
		height = heights[i]
		if height < minHeight:
			water += minHeight - height
		else:	
			water += 0
	return water