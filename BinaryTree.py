#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 15:59:54 2020

@author: Alaisha Naidu 
Name : Binary Tree 
Creds: LucidProgramming

"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None #initial left child is none
        self.right = None #initial right child is none
        
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def print_tree(self, traversal_type): #prints nodes according to how tree is traversed
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "") #pass tree root and empty string
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        else:
            print("traversal type" + str(traversal_type) + "is not supported")
            return False
    
    #PRE-ORDER (left until exhausted then right from each node)
    #1,2,4,5,3,6,7,
    def preorder_print(self, start, traversal):
        #Start at Root the move to Left subtree and then Right subtree
        if start:                               #if node is not none
            traversal += (str(start.value) + ",") #output separated by a comma
            traversal = self.preorder_print(start.left, traversal) #recursion starting at left child
            traversal = self.preorder_print(start.right, traversal) #then moving to right child
        return traversal
    
    #IN-ORDER (starting from left most node to root to right most node)
    #4,2,5,1,6,3,7,
    def inorder_print(self, start, traversal):
        if start: 
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + ",") 
            traversal = self.inorder_print(start.right, traversal)
        return traversal
        
    #POST-ORDER (starting from left, moving to right then to the root)
    #4,2,5,6,3,7,1,
    def postorder_print(self, start, traversal):
        if start: 
            traversal = self.inorder_print(start.left, traversal)
            traversal = self.inorder_print(start.right, traversal)
            traversal += (str(start.value) + ",") 
        return traversal
        
        
        
tree = BinaryTree(1)                #         1
tree.root.left = Node(2)            #       /   \
tree.root.right = Node(3)           #     2       3
tree.root.left.left = Node(4)       #    / \     / \
tree.root.left.right = Node(5)      #   4   5   6   7
tree.root.right.left = Node(6) 
tree.root.right.right = Node(7) 

print("Pre-order " + tree.print_tree("preorder"))
print("In-order " + tree.print_tree("inorder"))
print("Post-order " + tree.print_tree("postorder"))

#output:
#Pre-order 1,2,4,5,3,6,7,
#In-order 4,2,5,1,6,3,7,
#Post-order 4,2,5,6,3,7,1,