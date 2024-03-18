class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.parent = parent
        self.left = left
        self.right = right
        self.balance = 0
    

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.pivot = None
    
    def insert(self, data, setup):
        current = self.root
        parent = None

        while current is not None:
            parent = current
            if data <= current.data:
                current = current.left
            else:
                current = current.right
        
        new_node = Node(data, parent)    
        if parent is None:
            self.root = new_node
        elif data <= parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
        
        self.update_balances(new_node, setup)  
        return new_node
    
    def search(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return current
            elif data <= current.data:
                current = current.left
            else:
                current = current.right
        return None
    
    def update_balances(self, node, setup):
        self.pivot = None
        node_inserted = node
        parent = node.parent
        pivot_balance = 0

        while node is not None:
            if node.balance >= 1 or node.balance <= -1:
                if self.pivot is None:
                    self.pivot = node
                    pivot_balance = node.balance
            node.balance = self.calculate_balance(node)
            node = node.parent
            
        if self.pivot is None:
            if setup == 0:
                print("Case 1: No pivot found")
        else:
            if pivot_balance >= 1:
                if node_inserted.data < self.pivot.data and setup == 0:
                    print("Case 2: Pivot exists and the node was added to the shorter subtree")
                elif node_inserted.data > self.pivot.data and setup == 0:
                    if node_inserted.data > self.pivot.right.data:
                        self.left_rotate(self.pivot)
                        print("Case 3a: Adding a node to an outside subtree")
                    else:
                        print("Case 3b: Not supported")
            elif pivot_balance <= -1:
                if node_inserted.data > self.pivot.data and setup == 0:
                    print("Case 2: Pivot exists and the node was added to the shorter subtree")
                elif node_inserted.data < self.pivot.data and setup == 0:
                    if node_inserted.data < self.pivot.left.data:
                        self.right_rotate(self.pivot)
                        print("Case 3a: Adding a node to an outside subtree")
                    else:
                        print("Case 3b: Not supported")
                
    def calculate_balance(self, node):
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return right_height - left_height
    
    def height(self, node):
        if node is None:
            return 0
    
        queue = [node]
        height = 0
    
        while len(queue) > 0:
            size = len(queue)
            for i in range(size):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            height += 1
        return height

    def largest_balance(self):
        if self.root is None:
            return 0 
        
        balance_list = []
        stack = [self.root]
        
        while len(stack) > 0:
            node = stack.pop()
            balance = abs(node.balance)
            balance_list.append(balance)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        max_balance = max(balance_list)
        return max_balance
    
    def left_rotate(self, node): 
        pivot = node.right
        son = pivot.right
        temp = pivot
        node.right = son 
        if son:
            son.parent = node
        temp.right = son.left
        if son.left:
            son.left.parent = temp
        son.left = temp
        temp.parent = son

    def right_rotate(self, node):
        pivot = node.left
        son = pivot.left
        temp = pivot
        node.left = son
        if son:
            son.parent = node
        temp.left = son.right
        if son.right:
            son.right.parent = temp
        son.right = temp
        temp.parent = son

    
def main():
    BST = BinarySearchTree()

    BST.insert(10, 1)
    BST.insert(8, 1)
    BST.insert(11, 1)

    print("", end='')
    BST.insert(6, 0)

    BST = BinarySearchTree()
    BST.insert(10, 1)
    BST.insert(12, 1)
    BST.insert(13, 1)
    BST.insert(9, 1)
    print("\n", end='')
    BST.insert(8, 0)

    BST = BinarySearchTree()
    BST.insert(8, 1)
    BST.insert(9, 1)
    BST.insert(10, 1)
    BST.insert(11, 1)
    print("\n", end='')
    BST.insert(12, 0)

    BST = BinarySearchTree()
    BST.insert(8, 1)
    BST.insert(7, 1)
    BST.insert(12, 1)
    BST.insert(10, 1)
    BST.insert(13, 1)
    print("\n", end='')
    BST.insert(11, 0)


if __name__ == '__main__':
    main()
