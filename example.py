# Define the structure of a node in the linked list
class Node:
    def __init__(self, data):
        self.data = data   # Initialize the node's data
        self.next = None   # Initialize the pointer to the next node


# Function to traverse and print the linked list
def traverse_linked_list(head):
    current = head   # Start from the head of the linked list

    while current is not None:   # Loop until the end of the linked list
        print(current.data, end=" -> ")   # Print the data of the current node
        current = current.next   # Move to the next node
    print("None")


# Function to sort the linked list (using bubble sort)
def sort_linked_list(head):
    if head is None or head.next is None:  # If the list is empty or has only one node
        return head

    # Outer loop for iterations through the linked list
    swapped = True
    while swapped:
        swapped = False
        current = head
        while current.next is not None:
            if current.data > current.next.data:   # Compare adjacent nodes
                # Swap data between the nodes
                current.data, current.next.data = current.next.data, current.data
                swapped = True
            current = current.next

    return head


# Input list
input_list = [1, 3,10, 4, 5,100, 7, 9, 10]

# Create the linked list from the input list
head = None
for element in input_list:
    if head is None:
        head = Node(element)
        current = head
    else:
        current.next = Node(element)
        current = current.next

# Traverse the original linked list
print("Original linked list:")
traverse_linked_list(head)
print()

# Sort the linked list
head = sort_linked_list(head)

# Traverse the sorted linked list
print("Sorted linked list:")
traverse_linked_list(head)


