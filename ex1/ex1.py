class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent


class BST:
    def __init__(self):
        self.root = None

    def insert(data, root):
        if root is None:
            return Node(data)
        
        current = root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right

        if data <= parent.data:
            parent.left = Node(data, parent)
        else:
            parent.right = Node(data, parent)

        return root

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

        
def main():
    bst = BST()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    bst.insert(6)
    bst.insert(7)

    print(bst.search(5))
    print(bst.search(3))

if __name__ == "__main__":
    main()