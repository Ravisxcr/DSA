from root_data import *

import math
INT_INF = -math.inf

def getMax(root):
    if root is None:
        return INT_INF
    
    return max(getMax(root.left),getMax(root.right),root.data)


if __name__ == '__main__':
    print(getMax(root_1))
    print()
    print(getMax(root_m1))