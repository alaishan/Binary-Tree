#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:51:37 2020

@author: Alaisha Naidu
Name: Binary Tree Mirror
Creds: Shubham Singh and LucidProgramming
"""

#Define a node class for the nodes in the tree
class Node(object): 
    def __init__(self, value):
        self.value = value
        self.left = None #initial left child is none
        self.right = None #initial right child is none
        
    
def inorder_print(node): 
    if node == None:  
        return
          
    inorder_print(node.left)  
    print(node.value, end = ",")  
    inorder_print(node.right)  
        
def binary_tree_mirror(node):
    if node == None:
        return 
    else:
        temp = node 
        binary_tree_mirror(node.left)
        binary_tree_mirror(node.right)
        
        temp = node.left  # place holder for left node
        node.left = node.right  # new value for left node is previous value of right node
        node.right = temp # new value of right node is previous value of the left node



tree = Node(1)                 #         1
tree.left = Node(2)            #       /   \
tree.right = Node(3)           #     2       3
tree.left.left = Node(4)       #    / \     / \
tree.left.right = Node(5)      #   4   5   6   7
tree.right.left = Node(6) 
tree.right.right = Node(7) 

print("\nInorder traversal of the existing tree is ")  

inorder_print(tree) 

binary_tree_mirror(tree)

print("\nInorder traversal of the mirror tree is ")  
               
inorder_print(tree) 