''' Following are implemeted:
1. Queue class
2. BST insert
3. BST Search
4. BST delete
5. BST in order traversal
6. BST level order traversal
7. Find max node
'''
class Queue:
    def __init__(self):
        self.data = []

    def EnQueue(self, item):
        self.data.append(item)

    def DeQueue(self):
        item = self.data[0]
        self.data = self.data[1:]
        return item

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        root = Node(data)
        return
    if data < root.data:
        if root.left:
            insert(root.left, data)
        else:
            root.left = Node(data)
    else:
        if root.right:
            insert(root.right, data)
        else:
            root.right = Node(data)

def inorder(root):
    if root.left:
        inorder(root.left)
    print(root.data)
    if root.right:
        inorder(root.right)

def search(root, key):
    if root is None or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

def find_max(root):
    if root.right is None:
        print('Max is {}'.format(root.data))
        return root
    return find_max(root.right)

def level_order(root):
    if root is None:
        return    
    queue = Queue()
    queue.EnQueue(root)
    while len(queue.data) > 0:
        node = queue.DeQueue()
        print(node.data)
        if node.left:
            queue.EnQueue(node.left)
        if node.right:
            queue.EnQueue(node.right)

def delete(root, key):
    if root is None:
        return
    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        # Left node or both are empty
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None: # Right node is empty
            temp = root.left
            root = None
            return temp
        # both left & right nodes exist
        temp = find_max(root.left)
        root.data = temp.data
        delete(root.left, temp.data)
    return root

root = Node(5)
insert(root, 3)
insert(root, 9)
insert(root, 2)
insert(root, 6)
insert(root, 4)
insert(root, 10)
insert(root, 3)

print('Inorder Traversal...')
inorder(root)


find_max(root.left)
print('Level Order Traversal...')
level_order(root)

print('Found 4 at {}'.format(search(root, 4)))

delete(root, 4)
print('After deleting 4, Level Order Traversal...')
level_order(root)
