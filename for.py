# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    # Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete a node
    def delete_node(self, key):
        temp = self.head

        if temp and temp.data == key:
            self.head = temp.next
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Node not found!")
            return

        prev.next = temp.next

    # Print the linked list
    def display(self):
        temp = self.head
        if not temp:
            print("List is empty.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

# Main function with user input
if __name__ == "__main__":
    ll = LinkedList()
    
    while True:
        print("\n--- Linked List Operations ---")
        print("1. Append")
        print("2. Prepend")
        print("3. Delete Node")
        print("4. Display List")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            data = int(input("Enter data to append: "))
            ll.append(data)
        elif choice == '2':
            data = int(input("Enter data to prepend: "))
            ll.prepend(data)
        elif choice == '3':
            key = int(input("Enter value to delete: "))
            ll.delete_node(key)
        elif choice == '4':
            ll.display()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
