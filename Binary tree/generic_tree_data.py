from node import TreeNode_arr

n1 = TreeNode_arr(5)
n2 = TreeNode_arr(6)
n3 = TreeNode_arr(8)
n4 = TreeNode_arr(9)
n5 = TreeNode_arr(10)
n6 = TreeNode_arr(11)
n7 = TreeNode_arr(2)

n1.children.append(n2)
n1.children.append(n3)
n1.children.append(n4)
n1.children.append(n5)

n3.children.append(n6)
n3.children.append(n7)