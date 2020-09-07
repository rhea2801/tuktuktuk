class minMaxStack:
    def __init__(self):
        self.stack = []
        self.minMaxStack = []

    # ALL METHODS IN THIS CLASS (DATA STRUCTURE - STACK) ARE O(1)T, O(1)S

    def peek(self):
        return self.stack[len(self.stack)-1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            lastMinMax = self.minMaxStack[(self.minMaxStack)-1]
            newMinMax["min"] = min(number, lastMinMax["min"])
            newMinMax["max"] = max(number, lastMinMax["max"])
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack)-1]["min"]

    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack)-1]["max"]
