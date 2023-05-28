from root_data import *

# Naive Solution
def print_between(root,k1,k2):
    if root is None:
        return
    if root.data >= k1 and root.data <= k2:
        print_between(root.left,k1,k2)
        print(root.data, end=' ')
        print_between(root.right,k1,k2)
    elif root.data < k1 and root.data < k2:
        print_between(root.right,k1,k2)
    else:
        print_between(root.left,k1,k2)

# Little optimized solution
def print_between2(root,k1,k2):
    if root is None:
        return
    if root.data > k2:
        print_between2(root.left,k1,k2)
    elif root.data < k1:
        print_between2(root.right,k1,k2)
    else:
        print_between2(root.left,k1,k2)
        print(root.data, end=" ")
        print_between2(root.right,k1,k2)


if __name__ == "__main__":
    print_between(root_2,4,8)