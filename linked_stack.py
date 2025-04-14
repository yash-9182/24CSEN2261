class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None

    def push(self):
        data = int(input("Enter node data: "))
        new_node = StackNode(data)
        new_node.next = self.top
        self.top = new_node
        print(f"{data} pushed onto stack")

    def pop(self):
        if self.top is None:
            print("Stack Underflow")
            return
        popped_data = self.top.data
        self.top = self.top.next
        print(f"{popped_data} popped from stack")

    def display(self):
        if self.top is None:
            print("Stack is empty")
            return
        print("\nThe elements in the Stack are...")
        temp = self.top
        while temp:
            print(temp.data)
            temp = temp.next

def menu():
    print("\n1. Push \n2. Pop \n3. Display \n4. Exit")
    return int(input("Choose an option: "))

if __name__ == "__main__":
    stack = LinkedStack()
    while True:
        choice = menu()
        if choice == 1:
            stack.push()
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            stack.display()
        elif choice == 4:
            break
        else:
            print("Invalid Option")
