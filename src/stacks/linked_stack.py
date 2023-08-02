class Node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

class LinkedStack:
    def __init__(self):
        self.top = None
        self.length = 0
    
    def insert(self, value):
        self.top = Node(value, self.top)
        self.length += 1
        return True

    def remove(self):
        if self.length == 0:
            return False
        
        self.top = self.top.nextNode
        self.length -= 1
        return True
    
    def consult(self):
        if self.length == 0:
            return None
        return self.top.value

    def destroy(self):
        self.top = None
        self.length = 0
    
    def getLength(self):
        return self.length