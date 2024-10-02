class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return None  # Stack is empty

    def peek(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None  # Stack is empty

stack = MyStack()

while True:
    print("Choose an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        value = int(input("Enter the value to push: "))
        stack.push(value)
        print("Value pushed successfully!")
    elif choice == 2:
        popped_value = stack.pop()
        if popped_value is not None:
            print("Popped value:", popped_value)
        else:
            print("Stack is empty. Cannot pop.")
    elif choice == 3:
        peeked_value = stack.peek()
        if peeked_value is not None:
            print("Peeked value:", peeked_value)
        else:
            print("Stack is empty. Cannot peek.")
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please choose again.")