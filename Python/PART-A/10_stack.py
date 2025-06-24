stack = []
def push():
    item = input("Enter item to push: ")
    stack.append(item)
    print("Item pushed.")

def pop():
    if stack: print(f"{stack.pop()} popped.")
    else: print("Stack underflow!")

def display():
    if stack:
        print("Stack ites are:")
        i = len(stack) - 1
        while i >= 0:
            print(stack[i])
            i -= 1
    else: print("Stack is empty.")
        
while True:
    ch = input("\n1. Push\n2. Pop\n3. Display\n4. Exit\nEnter choice: ")
    if ch == '1': push()
    elif ch == '2': pop()
    elif ch == '3': display()
    elif ch == '4': break
    else: print("Invalid choice.")























#with desierd size

# stack = []
# n = int(input("Enter the size of the stack: "))

# def push():
#     if len(stack) < n:
#         stack.append(input("Enter item to push: "))
#         print("Item pushed.")
#     else:
#         print("Stack overflow!")

# def pop():
#     if stack:
#         print(f"{stack.pop()} popped.")
#     else:
#         print("Stack underflow!")

# def display():
#     if stack:
#         print("Stack ites are:")
#         i = len(stack) - 1
#         while i >= 0:
#             print(stack[i])
#             i -= 1
#     else:
#         print("Stack is empty.")

# while True:
#     ch = input("\n1. Push\n2. Pop\n3. Display\n4. Exit\nEnter choice: ")
#     if ch == '1': push()
#     elif ch == '2': pop()
#     elif ch == '3': display()
#     elif ch == '4': break
#     else: print("Invalid choice.")



















# my own 

# max = 4
# top = -1
# stack = [None] * max

# def push(data):
#     global top
#     if top == max - 1:
#         print("Stack is full")
#     else:
#         top += 1
#         stack[top] = data
#         print(f"{data} pushed")

# def pop():
#     global top
#     if top == -1:
#         print("Stack is empty")
#     else:
#         print(f"{stack[top]} popped")
#         stack[top] = None
#         top -= 1

# def peek():
#     print("Top:", stack[top] if top != -1 else "Stack is empty")

# def display():
#     print("Stack:", stack[:top+1] if top != -1 else "Empty")

# while True:
#     ch = int(input("\n1.Push  2.Pop  3.Peek  4.Display  5.Exit\nEnter ch: "))
#     if ch == 1:
#         push(input("Enter data: "))
#     elif ch == 2:
#         pop()
#     elif ch == 3:
#         peek()
#     elif ch == 4:
#         display()
#     elif ch == 5:
#         break
#     else:
#         print("Invalid ch")