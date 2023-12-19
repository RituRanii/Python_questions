class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None
    def print_LL(self):
        if self.head is None:
            print("Empty List")
        else:
            n = self.head
            while n is not None:
                print(n.data, end = "->")
                n = n.ref
            print("Null")
    # addition of data in the beginning of the linkedlist
    def add_at_beginning(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    def add_in_between(self,data,value):
        n = self.head
        while n is not None:
            if value == n.data:
                break
            n=n.ref
        if n is None:
            print("node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
        
    def add_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.add_at_beginning(data)
        else:
            n = self.head
            while n.ref is not None:
                n= n.ref
            n.ref = new_node

    def delete_begin(self):
        if self.head is None:
            print("Linked List is empty cant delete")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("Empty LL")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref = None

    def delete_by_value(self,x):
        if self.head is None:
            print("Empty LL")
            return
        if x == self.head.data:
            self.delete_begin()
        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("none")
        else:
            n.ref = n.ref.ref
LL1 = LinkedList()
# LL1.add_at_beginning(12)
LL1.add_at_end(100)
LL1.add_at_end(20)
LL1.add_at_beginning(10)
LL1.add_at_beginning(50)
LL1.add_in_between(200,10)
LL1.add_at_beginning(12)
LL1.add_at_end(39)
LL1.print_LL()
LL1.delete_begin()
LL1.delete_end()
LL1.delete_by_value(200)
LL1.print_LL()