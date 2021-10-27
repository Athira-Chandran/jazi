class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            print "The Stack is empty"
            return
        del_node = self.head
        self.head = self.head.next
        print "The top of the stack was: " + str(del_node.data)

    def peek(self):
        if self.head is None:
            print "The Stack is empty"
            return
        print "The top of the stack is: " + str(self.head.data)

    def print_stack(self):
        if self.head is None:
            print "The Stack is empty"
            return
        print "Stack items:\nHEAD ->",
        node = self.head
        while(node != None):
            print node.data,
            node = node.next
        print ""

stack = LinkedList()
continue_loop = True
while continue_loop:
    print "\nWhat do you want to do in the Stack using LinkedList?"
    print "1. Push"
    print "2. Pop"
    print "3. Peek"
    print "4. Print"
    print "5. Exit"
    choice = input("\nEnter your choice (1 - 5): ")
    if choice == 1:
        data = input("Enter the number to be pushed inside the stack: ")
        stack.push(data)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.peek()
    elif choice == 4:
        stack.print_stack()
    elif choice == 5:
        continue_loop = False
    else:
        print "Invalid choice"
