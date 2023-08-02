from hash_functions import *
from linked_list import *


class ContiguousTable:
    def __init__(self, maxLength, tableType="binary"):
        self.tableType = tableType.lower()
        self.length = 0
        
        if self.tableType in ["linear", "binary"]:
            self.maxLength = maxLength
        elif self.tableType == "hash":
            self.maxLength = findNextPrimeNumber(maxLength)
        
        self.key = [None] * self.maxLength
        self.value = [None] * self.maxLength
    
    def __repr__(self):
        if self.tableType in ["linear", "binary"]:
            return self.defaultRepresentation()
        elif self.tableType == "hash":
            return self.hashRepresentation()
        
    def insert(self, key, value):
        if self.tableType == "linear":
            return self.linearInsert(key, value)
        elif self.tableType == "binary":
            return self.binaryInsert(key, value)
        elif self.tableType == "hash":
            return self.hashInsert(key, value)

    def delete(self, key):
        if self.isEmpty():
            return False

        if self.tableType in ["linear", "binary"]:
            return self.defaultDelete(key)
        elif self.tableType == "hash":
            return self.hashDelete(key)
        
        self.length -=1

    def search(self, key):
        if self.isEmpty():
            return -1

        if self.tableType == "linear":
            return self.linearSearch(key)
        if self.tableType == "binary":
            return self.binarySearch(key)
        if self.tableType == "hash":
            return self.hashSearch(key)
    
    def consult(self, key):
        if self.isEmpty():
            return None
        
        if self.tableType in ["linear", "binary"]:
            return self.defaultConsult(key)
        elif self.tableType == "hash":
            return self.hashConsult(key)

    def destroy(self):
        if self.tableType == "hash":
            self.key = [None] * self.maxLength
            self.value = [None] * self.maxLength
        self.length = 0
    

    #insert options
    def linearInsert(self, key, value):
        position = self.search(key)
        if position == -1 and self.isFull():
            return False

        if position != -1:
            self.value[position] = value
        else:
            self.key[self.length] = key
            self.value[self.length] = value
            self.length += 1
        return True

    def binaryInsert(self, key, value):
        position = self.search(key)
        if position == -1 and self.isFull():
            return False
        
        if position != -1:
            self.value[position] = value
        elif self.isEmpty():
            self.key[0] = key
            self.value[0] = value
            self.length += 1
        else:
            sortedPosition = self.getSortedInsertPosition(key, 0, self.length - 1)
            for j in range(self.length - 1, sortedPosition - 1, -1):
                self.key[j+1] = self.key[j]
                self.value[j+1] = self.value[j]
                
            self.key[sortedPosition] = key
            self.value[sortedPosition] = value
            self.length += 1
        return True
    
    def getSortedInsertPosition(self, key, start, end):
        pivot = (start + end) // 2
        if start == end:
            if key > self.key[pivot]:
                return pivot + 1
            return pivot
        
        if key > self.key[pivot]:
            return self.getSortedInsertPosition(key, pivot + 1, end)
        else:
            return self.getSortedInsertPosition(key, start, pivot)
    
    def hashInsert(self, key, value):
        hashPosition, arrayPosition = self.hashSearch(key)
        if arrayPosition == -1 and self.isFull():
            return False
        
        if arrayPosition != -1:
            self.value[hashPosition].remove(arrayPosition)
            self.value[hashPosition].insert(value, arrayPosition)
            return True

        if self.key[hashPosition] == None:
            self.key[hashPosition] = LinkedList()
            self.value[hashPosition] = LinkedList()
        
        self.key[hashPosition].insert(key, 0)
        self.value[hashPosition].insert(value, 0)
        self.length += 1
        return True


    #delete options
    def defaultDelete(self, key):
        position = self.search(key)
        if position == -1:
            return False

        if position != self.length - 1:
                for i in range(position, self.length - 1):
                    self.key[i] = self.key[i+1]
                    self.value[i] = self.value[i+1]
        self.length -= 1
        return True

    def hashDelete(self, key):
        hashPosition, arrayPosition = self.hashSearch(key)
        
        if arrayPosition == -1:
            return False
        
        self.key[hashPosition].remove(arrayPosition)
        self.value[hashPosition].remove(arrayPosition)
        self.length -= 1
        return True


    #search options
    def linearSearch(self, key):
        for i in range(self.length):
            if key == self.key[i]:
                return i
        return -1
    
    def binarySearch(self, key):
        return self.binarySearchRecursion(key, 0, self.length - 1)
    
    def binarySearchRecursion(self, key, start, end):
        if start > end:
            return -1
        
        pivot = (start + end) // 2

        if key == self.key[pivot]:
            return pivot  
        elif key > self.key[pivot]:
            return self.binarySearchRecursion(key, pivot + 1, end)
        else:
            return self.binarySearchRecursion(key, start, pivot - 1)
        
    def hashSearch(self, key):
        hashPosition = calculateHash(key, self.maxLength)
        array = self.key[hashPosition]
        if array == None:
            arrayPosition = -1
        else:
            arrayPosition = array.search(key)
        return (hashPosition, arrayPosition)


    #consult options
    def defaultConsult(self, key):
        position = self.search(key)
        if position == -1:
            return None
        return self.value[position]
    
    def hashConsult(self, key):
        hashPosition, arrayPosition = self.search(key)
        return self.value[hashPosition].consult(arrayPosition)


    #representation options
    def defaultRepresentation(self):
        return f"{self.key[:self.length]}, {self.value[:self.length]}"
    
    def hashRepresentation(self):
        if self.length == 0:
            return "[], []"
        return f"{self.key}, {self.value}"


    #useful
    def isEmpty(self):
        return self.length == 0
        
    def isFull(self):
        return self.length == self.maxLength