import timeit
import random
import heapq

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LLPriorityQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, item):
        new_node = Node(item)
        if not self.head or self.head.value > item:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        while current.next and current.next.value < item:
            current = current.next
        
        new_node.next = current.next
        current.next = new_node

    def dequeue(self):
        if self.head:
            value = self.head.value
            self.head = self.head.next
            return value
        return None

class HeapPriorityQueue:
    def __init__(self):
        self.heap = []

    def enqueue(self, item):
        heapq.heappush(self.heap, item)

    def dequeue(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

def measure_execution_time(pq_class, operations):
    pq = pq_class()
    start_time = timeit.default_timer()
    for op, val in operations:
        if op == 'enqueue':
            pq.enqueue(val)
        else:
            pq.dequeue()
    total_time = timeit.default_timer() - start_time
    avg_time = total_time / len(operations)
    return total_time, avg_time

def generate_tasks(n=1000, enqueue_prob=0.7):
    tasks = []
    for _ in range(n):
        if random.random() < enqueue_prob:
            tasks.append(('enqueue', random.randint(1, 10000)))
        else:
            tasks.append(('dequeue', None))
    return tasks

def main():
    tasks = generate_tasks()
    list_pq_time, list_pq_avg = measure_execution_time(LLPriorityQueue, tasks)
    heap_pq_time, heap_pq_avg = measure_execution_time(HeapPriorityQueue, tasks)

    print(f"ListPriorityQueue: Total Time = {list_pq_time:.6f}s, Average Time per Task = {list_pq_avg:.6e}s")
    print(f"HeapPriorityQueue: Total Time = {heap_pq_time:.6f}s, Average Time per Task = {heap_pq_avg:.6e}s")

if __name__ == "__main__":
    main()
    

# Heap queue should be faster as inserting an element is of complexity O(logn) as opposed to  
# LL being complexity of O(n)
