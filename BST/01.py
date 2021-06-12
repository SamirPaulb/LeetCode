class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
    def insert(self,data):
        if self.key is None:
            self.key = BST(data)
            return
        if self.key == data:
            return
        if data < self.key:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
            return 
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)

root = BST(10)
ll = [2,4,53,5,3,2,4,434,232,42,242,23]
for i in ll:
    root.insert(i)
    

        

