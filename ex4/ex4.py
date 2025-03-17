# https://www.geeksforgeeks.org/building-heap-from-array/
import heapq
import random

class Heap:
    def __init__(self):
        self.data = []
        
    def heapify(self, arr):
        self.data = arr[:]
        heapq.heapify(self.data)
    
    def enqueue(self, val):
        heapq.heappush(self.data, val)
        
    def dequeue(self):
        if self.data:
            return heapq.heappop(self.data)
        return None
    
def testSorted():
    heap = Heap()
    sizes = [6, 1000, 5000, 10000]
    for size in sizes:
        arr = list(range(1, size + 1))
        heap.heapify(arr)
        assert heap.data == arr, f"Failed at size {size}: {heap.data}"

def testEmpty():
    heap = Heap()
    arr = []
    heap.heapify(arr)
    assert heap.data == [], f"Failed: {heap.data}"

def testRandom():
    heap = Heap()
    sizes = [100, 1000, 5000, 10000]
    for size in sizes:
        arr = random.sample(range(1, size + 1), size)
        heap.heapify(arr)
        expected = sorted(arr)
        for i in range(size):
            assert heap.dequeue() == expected[i], f"Failed at size {size}: {heap.data}"
    
    
def main():
    heap = Heap()
    arr = [10, 20, 15, 30, 40]
    print("Original array:", arr)
    heap.heapify(arr)
    print("Heapified array:", heap.data)
    
    heap.enqueue(5)
    print("After enqueue(5):", heap.data)
    
    dequeued = heap.dequeue()
    print("Dequeued element:", dequeued)
    print("After dequeue:", heap.data)

testSorted()
testEmpty()
testRandom()
print("All tests passed!")

if __name__ == "__main__":
    main()

            
    
