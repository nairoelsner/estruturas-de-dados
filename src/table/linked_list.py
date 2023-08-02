class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.nextNode = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        if self.length == 0:
            return "[]"
        
        string = '['
        current_node = self.head
        for i in range(self.length - 1):
            string += str(current_node.value) + ", "
            current_node = current_node.nextNode
        string += str(current_node.value) + ']'
        return string

    def insert(self, value, position):
        if position < 0 or position > self.length:
            return False

        if self.head == None or position == 0:
            self.head = Node(value, self.head)
        else:
            current_node = self.head
            current_position = 0
            while current_position < position - 1:
                current_node = current_node.nextNode
                current_position += 1
            current_node.nextNode = Node(value, current_node.nextNode)
        self.length += 1
        return True

    def remove(self, position):
        if position < 0 or position >= self.length:
            return False

        if position == 0:
            self.head = self.head.nextNode
        else:
            current_node = self.head
            current_position = 0
            while current_position < position - 1:
                current_node = current_node.nextNode
                current_position += 1
            current_node.nextNode = current_node.nextNode.nextNode
        self.length -= 1
        return True
    
    def search(self, value):
        current_node = self.head
        for i in range(self.length):
            if current_node.value == value:
                return i
            current_node = current_node.nextNode
        return -1
    
    def consult(self, position):
        if position < 0 or position >= self.length:
            return None
        
        current_node = self.head
        for i in range(position):
            current_node = current_node.nextNode
        return current_node.value

    def destroy(self):
        self.head = None
        self.length = 0
    
    def compare(self, list2):
        if self.length != list2.length:
            return False
        
        current_node1 = self.head
        current_node2 = list2.head

        while current_node1 != None:
            if current_node1.value != current_node2.value:
                return False
            current_node1 = current_node1.nextNode
            current_node2 = current_node2.nextNode
        return True
    
    def printReversed(self):
        print('[', end='')
        for i in range(self.length-1, 0, -1):
            print(self.consult(i), end=', ')
        print(f"{self.consult(0)}]")