from sys import argv

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def set_right(self, right):
        self.right = right
    
    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right
    
    def get_left(self):
        return self.left

def main():
    data = argv[1].replace(' ', '')
    indexes = []
    result = []
    for j, e in enumerate(data):
        if e == ')':
            end_index = j
            for i in range(end_index, -1, -1):
                if data[i] == '(' and i not in indexes:
                    start_index = i
                    indexes.append(i)
                    break
            result.append(data[start_index + 1: end_index])
    print(result)

    

if __name__ == '__main__':
    main()


