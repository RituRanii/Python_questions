class Node:
    def __init__(self, data):
        self.data = data  # Initialize the node with data
        self.next = None  # Initialize the next pointer to None


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list

    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:
            self.head = new_node  # If the list is empty, set the new node as the head
            return
        current = self.head
        while current.next:
            current = current.next  # Move to the last node in the list
        current.next = new_node  # Set the new node as the next node to the last node

    def traverse(self):
        current = self.head  # Start traversal from the head of the list
        while current:
            print(current.data, end="->")  # Print the data of the current node
            current = current.next  # Move to the next node in the list

# Creating a linked list and adding elements from the given input [1, 2, 4, 5, 6]
input_list = [1, 2, 4, 5, 6]
ll = LinkedList()

for item in input_list:
    ll.append(item)

# Traversing the linked list to display its elements
ll.traverse()

