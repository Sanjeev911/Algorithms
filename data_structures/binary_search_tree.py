# Implementation of binary Search Tree in Python

# Class Node represents a node of the tree
# Class Binarytree represents the binary tree
# The class methods implemented are inorder traversal, post-order traversal ,pre-order traversal,insert,delete and search etc.


class Node:
    def __init__(self,val):
        self.value = val
        self.right = None
        self.left = None
        self.level = None   #used to denote the level of each node in tthe tree

class Binarytree:
    def __init__(self,val = None):
        self.root = Node(val)

    def insert(self,val,node = None):
        if self.root.value == None:
            self.root = Node(val)
            return
        if node == None:
            node = self.root

        if val>node.value:
            if node.right == None:
                node.right = Node(val)
                return
            self.insert(val,node.right)
        if val<node.value:
            if node.left == None:
                node.left = Node(val)
                return
            self.insert(val,node.left)

    def inorder_traversal(self,node = None):
        if node == None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)
        print(node.value)
        if node.right:
            self.inorder_traversal(node.right)

    def preorder_traversal(self,node = None):
        if node == None:
            node = self.root
        print(node.value)
        if node.left:
            self.preorder_traversal(node.left)
        if node.right:
            self.preorder_traversal(node.right)

    def postorder_traversal(self,node = None):
        if node == None:
            node = self.root
        if node.left:
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node.value)

#***------------------ search function returns the key value if the key is found in the tree else returns none ----------***#
    def search(self,val,node = None):
        if node == None:
            node = self.root
        if node.value == val:
            return node.value
        if val>node.value and node.right != None:
            return self.search(val,node.right)
        if val<node.value and node.left != None:
            return self.search(val,node.left)

    def minValueNode(self,root):
        while(root.left is not None):
            root = root.left
        return root

    def delete(self,node,key):
        if node == None:
            return None
        if key < node.value:
            node.left = self.delete(node.left,key)
        elif key > node.value:
            node.right = self.delete(node.right,key)

        else:

            if node.left is None:
                temp  = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.minValueNode(node.right)

            node.value = temp.value
            node.right = self.delete(node.right,temp.value)

        return node

    def level_assign(self,root,level):
	    root.level = level
	    if root.right:
	        level_assign(root.right,level+1)
	    if root.left:
	        level_assign(root.left,level+1)

