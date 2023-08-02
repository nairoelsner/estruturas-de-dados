class ContiguousStack():
    def __init__(self, maxLength):
        self.maxLength = maxLength
        self.array = [None] * maxLength
        self.base = 0
        self.top = -1

    def insert(self, value):
        if self.getLength() == self.maxLength:
            return False

        self.top += 1
        self.array[self.top] = value
        return True
    
    def remove(self):
        if self.getLength() == 0:
            return False

        self.top -= 1
        return True
    
    def consult(self):
        if self.getLength() == 0:
            return None
        
        return self.array[self.top]
    
    def destroy(self):
        self.top = -1

    def getLength(self):
        return self.top + 1