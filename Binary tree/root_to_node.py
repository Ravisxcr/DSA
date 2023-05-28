from root_data import *

def rootToPath(root,data):
    if root is None:
        return
    if root.data == data:
        l = []
        l.append(root.data)
        return l
    left_data = rootToPath(root.left,data)
    if left_data is not None:
        left_data.append(root.data)
        return left_data
    
    right_data = rootToPath(root.right,data)
    if right_data is not None:
        right_data.append(root.data)
        return right_data
    
if __name__ == "__main__":

    print(rootToPath(root_2,1))
