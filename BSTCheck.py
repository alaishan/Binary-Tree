#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 20:49:44 2020

@author: Alaisha Naidu
Name: Binary Search Tree Check
"""

#Question 5
#Determine if a Binary tree is a binary search tree or not 
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None #initial left child is none
        self.right = None #initial right child is none

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def print_tree(self, traversal_type): #prints nodes according to how tree is traversed
        if traversal_type == "inorder":
            return self.inorder_print(tree.root, " ") #pass tree root and empty string
        else:
            print("traversal type" + str(traversal_type) + "is not supported")
            return False
   
 #IN-ORDER (starting from left most node to root to right most node)
    #4,2,5,1,6,3,7,
    def inorder_print(self, start, traversal):
        if start: 
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + " ")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
                    
            
tree = BinaryTree(6)                #         6
tree.root.left = Node(4)            #       /   \
tree.root.right = Node(8)           #     4       8
tree.root.left.left = Node(3)       #    / \     / \
tree.root.left.right = Node(5)      #   3   5   7   9  an in-order traversal will return an ordered list from smallest to largest value
tree.root.right.left = Node(7) 
tree.root.right.right = Node(9) 

print("In-order " + tree.print_tree("inorder"))

def Convert(string): 
    a_list = string.split()
    map_object = map(int, a_list)
    
    list_of_integers = list(map_object)
    return list_of_integers

def Check(list):
    x = 0
    y = len(list)-1
    while x < y:
        if list[x] < list[x+1]:
            print("true") 
            x += 1
            if x == y:
                print('This is a Binary Search Tree')
        else:
            print("Not a Binary Search Tree")
            return False
        
print(Convert(tree.print_tree("inorder")))
print(Check(Convert(tree.print_tree("inorder"))))