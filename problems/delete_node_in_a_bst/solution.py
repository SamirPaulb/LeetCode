class Solution:
    
    def findMin(self, root):
        current = root
        while current.left:
            current = current.left
        return current
    
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root
        
        #we want to get to a place where what we want to delete is root (==key), and everything less is on left and everything greater is on the right 
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else: # now we're at that point where root == key.val    
            
            #if what we want to delete is a leaf node
            if not root.left and not root.right:
                root = None #just make it none
            
            #it has one leaf node
            
            elif not root.left: #if there's right 
                root = root.right #make root equal to it's right. essentially deleting root

            elif not root.right: # similarly
                root = root.left

            else: #now it has two leaf nodes. we can either replace root's val with min of right, or max of left and still maintain bst property
                temp = self.findMin(root.right) #find min of right
                root.val = temp.val #change root's val to min of right's val
                root.right = self.deleteNode(root.right, temp.val) #delete that temp.val from right subtree. 
        
        return root