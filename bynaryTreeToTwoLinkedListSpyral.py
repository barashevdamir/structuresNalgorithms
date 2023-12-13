# Реализация обхода дерева по спирали

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None  # Для двухсвязного списка

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

def spiral_tree_to_list(root):
    if not root:
        return None

    dll = DoublyLinkedList()
    stack1 = [root]
    stack2 = []

    while stack1 or stack2:
        while stack1:
            current = stack1.pop()
            dll.append(current.value)
            if current.right:
                stack2.append(current.right)
            if current.left:
                stack2.append(current.left)

        while stack2:
            current = stack2.pop()
            dll.append(current.value)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)

    return dll

# Тестирование
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

dll = spiral_tree_to_list(root)
current = dll.head
while current:
    print(current.value, end=" -> ")
    current = current.next
