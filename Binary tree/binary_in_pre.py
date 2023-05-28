from root_data import *
import print_relation

def buildTree(inn, pre, ins, ine):
    global preIndex, mp

    if ins > ine:
        return
    
    curr = pre[preIndex]
    preIndex+= 1
    tNode = BinaryNode(curr)

    if ins == ine:
        return tNode
    
    inIndex = mp[curr]

    tNode.left = buildTree(inn, pre, ins, inIndex-1)
    tNode.right = buildTree(inn, pre, inIndex+1, ine)

    return tNode

def buildTreeWrap(inn, pre, lenn):
    global mp

    for i in range(lenn):
        mp[inn[i]] = i
    
    return buildTree(inn,pre,0,lenn-1)

if __name__ == '__main__':
    len1 = len(pre_1)
    mp = {}
    preIndex = 0
    
    root = buildTreeWrap(in_1,pre_1,len1)
    print_relation.printTree2(root)