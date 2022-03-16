from hashlib import new
from tkinter import N


class Node:
    def __init__(self, initial_data):
        self.data = initial_data
        self.next = None

    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head= None
        self.tail= None
    
    def append(self, new_node):
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self) -> str:
        cur_node = LL.head
        str_ = ""
        while cur_node != None:
            str_ += str(cur_node.data)
            cur_node = cur_node.next
            if cur_node != None:
                str_ += "->"
        return str_


if __name__ == '__main__':
    LL = LinkedList()

    a = Node(5)
    b = Node(34)
    c = Node(66)
    d = Node(80)
    e = Node(97)

    LL.append(a)
    LL.append(e)
    LL.append(c)

    print(LL)




