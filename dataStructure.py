class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
              print(current.data, end=" ")
              current = current.next
        print()
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current:
            prev.next = current.next


linked_list = LinkedList()


linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.insert(4)


print("Initial Linked List:")
linked_list.display()


linked_list.insert(5)
print("After inserting a new node (5):")
linked_list.display()


linked_list.delete(2)
print("After deleting an existing node (2):")
linked_list.display()
