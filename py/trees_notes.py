# Tree starts at the root and fans out through branches
# Collection of trees are called are forrest
# Extension of Linked list

# Individual elements in a tree is called a node, must be completely connected
# No cycles allowed in a tree

# You can describe a tree in terms of levels, how many connections it takes to get to root
# Parent child relationship described

# Nodes at the end with no children is called a leaf

# height of a tree is how far a node is from the leaf

"""
Tree Traversal

Two Main Types


DFS: Depth First Search
    - PostOrder Traversal
        i. Only check off node when we have seen all of its' descendants

    - PreOrder Traversal
        i. Only check off node when we have seen its' left child and come back to it

     - InOrder Traversal
        i. Start root, pick left (by convention) child until hit leaf
            now move up to parent and check right, continue until you have seen everything

BFS: Breadth First Search
    - Level Order Traversal
        i. Start at left most level and most to the right until you get to the bottom

"""

"""
Binary Tree

"""