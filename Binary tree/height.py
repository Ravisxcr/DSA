from root_data import *

def height(root):
    if root is None:
        return 0
    
    ld = height(root.left)
    rd = height(root.right)

    if ld > rd:
        return ld + 1
    else:
        return rd + 1
    

if __name__ == '__main__':
    print(height(root_1)," ",height(root_m1), " ",height(root_m2))
