import numpy as np
import timeit

class TreeNode:
    def __init__(self, data, parent=None, left=None, right=None):
        self.parent = parent
        self.data = data
        self.left = left
        self.right = right
    
def insert(data, root=None):
    current = root
    parent = None
    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right
            
    if root is None:
        root = TreeNode(data)
    elif data <= parent.data:
        parent.left = TreeNode(data, parent)
    else:
        parent.right = TreeNode(data, parent)
            
def search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return None

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index)
        quicksort(arr, pivot_index + 1, high)
        
def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True
        else: 
            arr[left], arr[right] = arr[right], arr[left]
    arr[low], arr[right] = arr[right], arr[low]
    return right

def binarySearch(arr, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, low, mid-1, x)
        else:
            return binarySearch(arr, mid + 1, high, x)
    else:
        return -1

def main():
    theList = [x for x in range(10000)]
    theVector = np.array(theList)
    np.random.shuffle(theVector)
    grandTotalTimeBST = 0
    grandTotalTimeBS = 0
    root = TreeNode(theVector[0])
    for e in theVector[1:]:
        insert(e, root)
    quicksort(theVector, 0, 9999)
    for i in theList:
        totalTimeBST = 0
        totalTimeBS = 0
        for j in range(10):
            totalTimeBST += timeit.timeit(lambda: search(i, root))
            totalTimeBS += timeit.timeit(lambda: binarySearch(theVector, 0, 9999, i))
        averageTimeBST = totalTimeBST / 10
        averageTimeBS = totalTimeBS / 10
        grandTotalTimeBST += totalTimeBST
        grandTotalTimeBS += totalTimeBS
        print(f'Total time to search for {i} 10 times in a binary search tree: {totalTimeBST:.3f}')
        print(f'Average time to search for {i} in a binary search tree: {averageTimeBST:.3f}')
        print(f'Total time to binary search for {i} 10 times in a vector is: {totalTimeBS:.3f}')
        print(f'Average time to binary search for {i} in a vector is: {averageTimeBS:.3f}')
    grandAverageTimeBST = grandTotalTimeBST / 100000
    grandAverageTimeBS = grandTotalTimeBS / 100000
    print(f'Total time to search for each element 10 times in a binary search tree: {grandTotalTimeBST}')
    print(f'Average time to search for an element in a binary search tree: {grandAverageTimeBST}')
    print(f'Total time to binary search for each element 10 times in a vector: {grandTotalTimeBS}')
    print(f'Average time to binary search for an element in a vector: {grandAverageTimeBS}')
    
#4. Searching through a binary search tree is faster. This is because in a binary search tree, nodes are arranged in way that causes each comparison to skip around half of whats of the tree. Binary search does the same, but it requires the middle element to be the value we are searching for, leading to it having to make more comparisons.
    
if __name__ == '__main__':
    main()