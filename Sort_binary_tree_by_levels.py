#!/usr/bin/env python3

#https://www.codewars.com/kata/52bef5e3588c56132c0003bc

class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n
        
def tree_by_levels(node):
    if(node == None):
        return []
    queue = [node]
    result = []
    
    while(len(queue) > 0):
        node_cur = queue.pop(0)
        result.append(node_cur.value)
        if(node_cur.left != None):
            queue.append(node_cur.left)
        if(node_cur.right != None):
            queue.append(node_cur.right)
    
    return result
    
    
def main():
    assert(tree_by_levels(None) == [])
    assert(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)) == [1, 2, 3, 4, 5, 6])
    
if(__name__ == '__main__'):
    main()
    
    
