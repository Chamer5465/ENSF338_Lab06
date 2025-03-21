from sys import argv

class TreeNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def set_data(self, data):
        self.data = data
    
    def set_right(self, right):
        self.right = right
    
    def set_left(self, left):
        self.left = left

    def get_data(self):
        return self.data
    
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
                elif i.isdigit() == False and count == 0 and j > 0:
                    left = TreeNode()
                    right = TreeNode()
                    self.data = i
                    if ''.join(data_list[1:j]).isdigit():
                        left.set_data(int(''.join(data_list[1:j])))
                        self.left = left
                    else:
                        left.insert(' '.join(data_list[1:j]))
                        self.left = left
                    if ''.join(data_list[j + 1:-1]).isdigit():
                        right.set_data(int(''.join(data_list[j + 1:-1])))
                        self.right = right
                    else:
                        right.insert(' '.join(data_list[j + 1:-1]))
                        self.right = right
                        
    def post_order_calc(self):
        if self.left == None and self.right == None:
            return
        
        self.left.post_order_calc()

        self.right.post_order_calc()
        
        match self.data:
            case '+':
                self.data = self.left.data + self.right.data
            case '-':
                self.data = self.left.data - self.right.data
            case '*':
                self.data = self.left.data * self.right.data
            case '/':
                self.data = self.left.data // self.right.data
    
    
    
    
                    
                
            

def main():
    data = argv[1]
    count = 0
    for i in data:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
    if count == 0:
        root = TreeNode()
        root.insert(data)
        root.post_order_calc()
        print(root.data)
    else:
        print('Invalid expression: Opening and closing parenthases are not equal.')
    
if __name__ == '__main__':
    main()


