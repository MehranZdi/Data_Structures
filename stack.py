import numpy as np


class Stack:
    def __init__(self):
        self.top = -1
        self.stack = np.array(())

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
        return f'The stack is: {self.stack} and the value of "top" is: {self.top}'


if __name__ == '__main__':
    stack_0 = Stack()
    stack_0.push(3)
    stack_0.push(6)
    stack_0.pop()
    stack_0.pop()
    stack_0.pop()