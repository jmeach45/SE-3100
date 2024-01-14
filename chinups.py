class listmanager:

    def __init__(self):
        self.list = []

    def addToList(self, val):
        self.list.append(val)
    
    def removeFromList(self):
        if not self.isEmpty():
            return self.list.pop(0)
        else:
            return "Queue is empty"

    def isEmpty(self):
        return len(self.list) == 0

    def size(self):
        return len(self.list)

    def printList(self):
        print("Current items in the list:", self.list)