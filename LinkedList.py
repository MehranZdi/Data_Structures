class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == '__main__':
    linked_list = LinkedList()
    first_node = Node(1)
    linked_list.head = first_node
    second_node = Node(2)
    third_node = Node(3)

    first_node.next = second_node
    second_node.next = third_node
    while linked_list.head is not None:
        print(linked_list.head.data)
        linked_list.head = linked_list.head.next
