class ContiguousList:
    def __init__(self, maxLengthLength):
        self.maxLength = maxLengthLength
        self.array = [None] * maxLengthLength
        self.start = -1
        self.end = -1
    
    def __repr__(self):
        if self.isEmpty():
            return "[]"
        
        string = "["
        for i in range(self.start, self.end):
            string += str(self.array[i]) + ", "
        
        return string + str(self.array[self.end]) + ']'
    
    def insert(self, value, position):
        if self.isFull():
            return False
        
        if position < 0 or position > self.getLength():
            return False
        
        if self.isEmpty():
            self.start = self.maxLength // 2
            self.end = self.start
        else:
            start_distance = position
            end_distance = self.end - (self.start + position)
            
            if (start_distance >= end_distance and self.end != self.maxLength - 1) or self.start == 0:
                for i in range(self.end, self.start + position - 1, -1):
                    self.array[i+1] = self.array[i]
                self.end += 1
            else:
                for i in range(self.start, self.start + position):
                    self.array[i-1] = self.array[i]
                self.start -= 1
                
        self.array[self.start + position] = value
        return True
        
    def remove(self, position):
        if self.isEmpty():
            return False
        
        if position < 0 or position >= self.getLength():
            return False

        if position == 0:
            self.start += 1
        elif position == self.getLength() - 1:
            self.end -= 1
        elif position <= self.end - (self.start + position):
            for i in range(self.start + position - 1, self.start, -1):
                self.array[i] = self.array[i-1]
            self.start += 1
        else:
            for i in range(self.start + position - 1, self.end):
                self.array[i] = self.array[i+1]
            self.end -= 1
        return True
    
    def search(self, value):
        for i in range(self.start, self.end + 1):
            if self.array[i] == value:
                return i - self.start
        return -1
    
    def consult(self, position):
        if position < 0 or position >= self.getLength():
            return None
        return self.array[self.start + position]
    
    def destroy(self):
        self.start = -1
        self.end = -1
    
    #useful
    def isEmpty(self):
        return self.start == -1 or self.end == -1

    def isFull(self):
        return self.start == 0 and self.end == self.maxLength - 1
    
    def getLength(self):
        if self.isEmpty():
            return 0
        return self.end - self.start + 1