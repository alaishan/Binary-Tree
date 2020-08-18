#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:42:04 2020

@author: Alaisha Naidu
Name: Binary Tree Search
Creds: LucidProgramming

"""
#In a binary search tree all nodes connected to the left of a node is less than the value of the current node

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root is None: #check if root is none/ if it exists
            self.root = Node(data) #if not, create a root with input data 
        else: 
            self._insert(data, self.root)
        
    def _insert(self, data, current_node): #finds location for new node through recursion
        if data < current_node.data: #less than ie left
            if current_node.left is None: #if the left child of current node is none
                current_node.left = Node(data) #assign input to left child 
            else:
                self._insert(data, current_node.left) #recursive step
        
        elif data > current_node.data: #greater than ie right
             if current_node.right is None: #if the right child of current node is none
                current_node.right = Node(data) #assign input to right child 
             else:
                self._insert(data, current_node.right) #recursive step
        
        else:
            print("Value already exists in tree") #no duplicate values 
    
    def find(self, data):
        if self.root: #if the root is not none
            is_found = self._find(data, self.root) #will return a boolean value to indicate if the value is in the tree or not
            if is_found:
                return True
            return False #if not found in the existing tree
        else: #if no nodes in the tree
            return None
        
    def _find(self, data, current_node):
        if data > current_node.data and current_node.right: #if input data is greater than current node and it has a right child
            return self._find(data, current_node.right) #recursive call
        elif data < current_node.data and current_node.left: #if input data is less than current node and it has a left child
            return self._find(data, current_node.left) 
        if data == current_node.data: #if it is in the tree return True
            return True

binarysearchtree = BinarySearchTree()

binarysearchtree.insert(4)
binarysearchtree.insert(2)
binarysearchtree.insert(8)
binarysearchtree.insert(5)
binarysearchtree.insert(10)

print(binarysearchtree.find(4))
                
    
        
