class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        if temp is None:
            print("Linked list is empty.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

if __name__ == "__main__":
    ll = LinkedList()

    print("Enter numbers to add to the linked list. Type 'done' to stop.")

    while True:
        user_input = input("Enter a number: ")
        if user_input.lower() == "done":
            break
        try:
            num = int(user_input)
            ll.append(num)
        except ValueError:
            print("Please enter a valid number or 'done'.")

    print("Your Linked List:")
    ll.display()
