def naive_part(a,p):
    part = a[p]
    b = [part]
    for i in range(len(a)):
        if i==p:
            continue
        if a[i] <= part:
            b.insert(0,a[i])
        else:
            b.append(a[i])
    a=b
    del b
    return a

def lamuto_part(a,p):
    h = len(a)-1
    pivot = a[h]
    i = -1
    for j in range(h+1):
        if a[j] < pivot:
            i+=1
            a[i],a[j] = a[j],a[i]
    a[i+1],a[h] = a[h],a[i+1]
    return a



if __name__ == "__main__":
    a = [3,8,6,12,8,7,90,1,2,70]
    p = 9
    print(lamuto_part(a,p))
