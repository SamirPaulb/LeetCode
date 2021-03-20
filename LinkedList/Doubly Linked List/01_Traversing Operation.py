class Node:
    def __init__(self,data):
        self.data = data
        self.nref = None
        self.pref = None
class DoublyLL:
    def __init__(self):
        self.head = None
    
    def print_DLL(self):
        if self.head is None:
            print("The Linked List is Empty")
        else:
            n = self.head
            while n is not None:
                print(n.data,"--->",end="")
                n = n.nref

DLL = DoublyLL()
DLL.print_DLL()
