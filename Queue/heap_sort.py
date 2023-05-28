def heapify_down(arr,i,n):
    parent_Index = i
    left_index = 2*parent_Index + 1
    right_index = 2*parent_Index + 2
    
    while left_index < n:
        minIndex = parent_Index
        if arr[minIndex] > arr[left_index]:
            minIndex = left_index
        if right_index < n and arr[minIndex] > arr[right_index]:
            minIndex = right_index

        if minIndex == parent_Index:
            return
        arr[minIndex], arr[parent_Index] = arr[parent_Index], arr[minIndex]
        parent_Index = minIndex
        left_index = 2*parent_Index + 1
        right_index = 2*parent_Index + 2

def heapify_up(arr,i,n):
    parent_Index = i
    left_index = 2*parent_Index + 1
    right_index = 2*parent_Index + 2
    
    while left_index < n:
        minIndex = parent_Index
        if arr[minIndex] < arr[left_index]:
            minIndex = left_index
        if right_index < n and arr[minIndex] < arr[right_index]:
            minIndex = right_index

        if minIndex == parent_Index:
            return
        arr[minIndex], arr[parent_Index] = arr[parent_Index], arr[minIndex]
        parent_Index = minIndex
        left_index = 2*parent_Index + 1
        right_index = 2*parent_Index + 2

def heap_asc(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range((i+1)//2-1, -1, -1):
            heapify_up(arr, j, i+1)
        arr[0], arr[i] = arr[i], arr[0]

def heap_desc(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range((i+1)//2-1, -1, -1):
            heapify_down(arr, j, i+1)
        arr[0], arr[i] = arr[i], arr[0]

arr = [4,6,3,9,11,10]
n= len(arr)
heap_asc(arr)


for i in range(n):
    print(arr[i], end=" ")
