class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        elif self.key < data:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
            return
        elif self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
            return
    def search(self,data):
        if self.key == data:
            print("Node is Found")
            return
        if self.key < data:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is NOT found")
            return
        if self.key > data:
            if self.lchild:
                delf.lchild.search(data)
            else:
                print("Node is NOT found")


        
root = BST(10)
ll = [1,2,33,23,12,33,12,12,31,12,222,333,456,6667,77777,51]
for i in ll:
    root.insert(i)
root.search(222)

    

        

