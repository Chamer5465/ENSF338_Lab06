from sys import argv

class TreeNode:
    def __init__(self):
        self.data = None
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
    
    def insert(self, data):
        if '(' not in data:
            self.data = int(data)
        else:
            data_list = data.split(' ')
            count = 0
            for j, i in enumerate(data_list):
                if i == '(' and j > 0:
                    count += 1
                elif i == ')':
                    count -= 1
                elif i.isdigit() == False and count == 0:
                    self.data = i
                    if ''.join(data_list[1:j]).isdigit():
                        self.left = data_list[1:j].join()
                    else:
                        self.insert(' '.join(data_list[1:j]))
                    if ''.join(data_list[j + 1:-1]).isdigit():
                        self.left = data_list[j + 1:-1].join()
                    else:
                        self.insert(' '.join(data_list[j + 1:-1]))
                    
                
            

def main():
    data = argv[1]
    root = TreeNode()
    root.insert(data)
    print('Insert Completed')
    """for j, e in enumerate(data):
        if e == ')':
            end_index = j
            for i in range(end_index, -1, -1):
                if data[i] == '(' and i not in indexes:
                    start_index = i
                    indexes.append(i)
                    break
            result.append(data[start_index + 1: end_index])
    print(result)
"""
    

if __name__ == '__main__':
    main()


