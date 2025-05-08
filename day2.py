class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, index, data):
        if index == 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            if current is None:
                print("Position out of range")
                return
            current = current.next
        if current is None:
            print("Position out of range")
            return
        new_node.next = current.next
        current.next = new_node

    def delete_by_value(self, data):
        current = self.head
        if current and current.data == data:
            self.head = current.next
            return
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next
        if current:
            prev.next = current.next
        else:
            print("Value not found")

    def delete_at_position(self, index):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        if index == 0:
            self.head = current.next
            return
        for _ in range(index - 1):
            if current is None:
                print("Position out of range")
                return
            current = current.next
        if current is None or current.next is None:
            print("Position out of range")
            return
        current.next = current.next.next

    def search(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev
ll = LinkedList()

while True:
    print("\n--- Linked List Menu ---")
    print("1. Insert at Beginning")
    print("2. Insert at End")
    print("3. Insert at Position")
    print("4. Delete by Value")
    print("5. Delete by Position")
    print("6. Search for Value")
    print("7. Count Nodes")
    print("8. Reverse List")
    print("9. Display List")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        val = int(input("Enter value to insert at beginning: "))
        ll.insert_at_beginning(val)
    elif choice == "2":
        val = int(input("Enter value to insert at end: "))
        ll.insert_at_end(val)
    elif choice == "3":
        pos = int(input("Enter position: "))
        val = int(input("Enter value: "))
        ll.insert_at_position(pos, val)
    elif choice == "4":
        val = int(input("Enter value to delete: "))
        ll.delete_by_value(val)
    elif choice == "5":
        pos = int(input("Enter position to delete: "))
        ll.delete_at_position(pos)
    elif choice == "6":
        val = int(input("Enter value to search: "))
        index = ll.search(val)
        if index != -1:
            print(f"Value found at position {index}")
        else:
            print("Value not found")
    elif choice == "7":
        print("Total nodes:", ll.count())
    elif choice == "8":
        ll.reverse()
        print("List reversed")
    elif choice == "9":
        ll.display()
    elif choice == "0":
        print("Exiting program.")
        break
    else:
        print("Invalid choice! Try again.")
