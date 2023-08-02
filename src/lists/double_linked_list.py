class Node:
    def __init__(self, value, next_node=None, previous_node=None):
        self.value = value
        self.nextNode = next_node
        self.previousNode = previous_node

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    #função para dar print na lista
    def __repr__(self):
        if self.length == 0:
            return "[]"
        
        current_node = self.head
        string = '['
        for i in range(self.length - 1):
            string += str(current_node.value) + ", "
            current_node = current_node.nextNode
        string += str(current_node.value) + ']'
        return string

    #função para inserir elemento na lista
    def insert(self, value, position):
        if position < 1 or position > self.length + 1:
            return

        if self.length == 0:
            self.head = Node(value)
            self.tail = self.head

        elif position == 1:
            self.head.previousNode = Node(value, self.head, None)
            self.head = self.head.previousNode
        
        else:
            current_node = self.head

            if position == self.length + 1:
                while current_node.nextNode != None:
                    current_node = current_node.nextNode

                current_node.nextNode = Node(value, None, current_node)
                self.tail = current_node.nextNode
            else:
                current_position = 1
                while current_position < position - 1:
                    current_node = current_node.nextNode
                    current_position += 1
                current_node.nextNode = Node(value, current_node.nextNode, current_node)
        
        self.length += 1

    #função para remover elemento da lista
    def remove(self, position):
        if position < 1 or position > self.length:
            return False

        if self.length == 1:
            self.head = None
            self.tail = None
        
        elif position == 1:
            self.head = self.head.nextNode
            self.head.previousNode = None
        
        else:
            current_node = self.head
            current_position = 1
            while current_position < position - 1:
                current_node = current_node.nextNode
                current_position += 1

            if position == self.length:
                current_node.nextNode = None
                self.tail = current_node
            else:
                current_node.nextNode = current_node.nextNode.nextNode
                current_node.nextNode.previousNode = current_node

        self.length -= 1
        return True
    
    #função para verificar posição de um elemento
    def position(self, value):
        current_node = self.head
        for i in range(1, self.length + 1):
            if current_node.value == value:
                return i
            current_node = current_node.nextNode
        return None
    
    #função para verificar o elemento em uma posição
    def value(self, position):
        if position < 1 or position > self.length:
            return None

        if position > self.length / 2:
            current_node = self.tail
            for i in range(self.length - position + 1):
                current_node = current_node.previousNode
            return current_node.value
        
        current_node = self.head
        for i in range(position - 1):
            current_node = current_node.nextNode
        return current_node.value
    
    def destroy(self):
        while self.remove(1):
            pass

    def printReversed(self):
        if self.length == 0:
            print("[]")
        

        current_node = self.tail
        string = '['

        for i in range(self.length - 1):
            string += str(current_node.value) + ', '
            current_node = current_node.previousNode
        string += str(current_node.value) + ']'
        print(string)