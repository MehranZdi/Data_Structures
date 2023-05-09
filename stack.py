import numpy as np

class Stack:
    def __init__(self, name):
        self.top = -1
        self.name = name
        self.stack = np.array(())
        print(f' --- {self.name} stack has been created. ---')

    def push(self, number):
        self.stack = np.append(self.stack, number)
        self.top += 1
        print(self)

    def pop(self):
        if self.top != -1:
            self.stack = np.delete(self.stack, self.top)
            self.top -= 1
            print(self)
        else:
            print("stack in empty!")

    def __str__(self):
        return f'The {self.name} stack is: {self.stack} and the value of "top" is: {self.top}'


if __name__ == '__main__':
    proceed = 'Yes'
    while proceed == 'Yes':
        stack_choice = input("Press 1 to create a stack: ")
        match stack_choice:
            case '1':
                stack_name = input("Enter your preferred stack name: ")
                stack = Stack(stack_name)
                current_stack = 'Yes'
                while current_stack == 'Yes':
                    operation = input("Press 1 to push an item to the stack: \nPress 2 to pop an item from the stack:\n")
                    match operation:
                        case '1':
                            data = int(input('Enter the value: '))
                            stack.push(data)
                        case '2':
                            stack.pop()
                    current_stack = input("Keep changing the current stack? (Yes/No): ")
        proceed = input("Do you want to proceed? (Yes/No): ")
