class Node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

class LinkedQueue:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0

    def insert(self, value):
        new_node = Node(value)
        if self.start == None:
            self.start = new_node
            self.end = new_node
        else:
            self.end.nextNode = new_node
            self.end = new_node

        self.length += 1
        return True

    def remove(self):
        if self.length == 0:
            return False
        self.start = self.start.nextNode
        self.length -= 1
        return True

    def consult(self):
        if self.length == 0:
            return None
        return self.start.value
    
    def destroy(self):
        self.start = None

    def getLength(self):
        return self.length
