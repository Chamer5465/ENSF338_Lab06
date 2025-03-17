import random
import timeit

class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        current = self.root
        while True:
            if data <= current.data:
                if current.left is None:
                    current.left = Node(data, current)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(data, current)
                    break
                else:
                    current = current.right

    def search(self, data):
        current = self.root
        while current is not None:
            if current.data == data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None

def build_tree_from_list(data_list):
    tree = BST()
    for item in data_list:
        tree.insert(item)
    return tree

def measure_search_time(tree, data_list):
    total_time = timeit.timeit(lambda: [tree.search(x) for x in data_list], number=10)
    avg_time_per_search = total_time / (len(data_list) * 10)
    return avg_time_per_search, total_time

def main():

    sorted_vector = list(range(10000))

    tree_sorted = build_tree_from_list(sorted_vector)
    
    avg_time_sorted, total_time_sorted = measure_search_time(tree_sorted, sorted_vector)
    
    print("built from sorted vector:")
    print(f"Average search time per element: {avg_time_sorted} seconds")
    print(f"Total search time: {total_time_sorted} seconds")
    
    shuffled_vector = sorted_vector.copy()
    random.shuffle(shuffled_vector)
    
    tree_shuffled = build_tree_from_list(shuffled_vector)
    
    avg_time_shuffled, total_time_shuffled = measure_search_time(tree_shuffled, sorted_vector)
    
    print("built from shuffled vector:")
    print(f"Average search time per element: {avg_time_shuffled} seconds")
    print(f"Total search time: {total_time_shuffled} seconds")

if __name__ == "__main__":
    main()

#The bst built froom the shuffled vector is significantly faster for searches.
#The bst built from the sorted vector is slower for searches. 
#This is due to the fact that the sorted vector produces a less balanced tree leading to a less efficient search time.