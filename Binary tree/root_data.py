from node import BinaryNode

"""
Constructed binary tree is:
     1
    / \
    2  3
   / \  \
  4   5  8
        / \
        6  7
"""

root_1 = BinaryNode(1)
root_1.left = BinaryNode(2)
root_1.right = BinaryNode(3)
root_1.left.left = BinaryNode(4)
root_1.left.right = BinaryNode(5)
root_1.right.right = BinaryNode(8)
root_1.right.right.left = BinaryNode(6)
root_1.right.right.right = BinaryNode(7)


"""         1              
           / \
           2  3
          / \
          4  5
"""
root_m1 = BinaryNode(1)
root_m2 = BinaryNode(1)

root_m1.left = BinaryNode(2)
root_m1.right = BinaryNode(3)
root_m1.left.left = BinaryNode(4)
root_m1.left.right = BinaryNode(5)

root_m2.left = BinaryNode(3)
root_m2.right = BinaryNode(2)
root_m2.right.left = BinaryNode(5)
root_m2.right.right = BinaryNode(4)


in_1 = [40,20,60,50,70,10,80,100,30]
pre_1 = [10,20,40,50,60,70,30,80,100]

in_2 = [20,10,40,30,50]
pre_2 = [10,20,30,40,50]


# Sorted Binary tree for BST
root_2 = BinaryNode(5)
root_2.left = BinaryNode(3)
root_2.right = BinaryNode(7)
root_2.left.left = BinaryNode(2)
root_2.left.right = BinaryNode(4)
root_2.left.left.left = BinaryNode(1)
root_2.right.left = BinaryNode(6)
root_2.right.right = BinaryNode(8)