# -*- coding: utf-8 -*-


class Node:
    def __init__(self, data=None,):
        self.data = data
        self.next = None


class LinkList:
    def __init__(self, node=None):
        self.head = node
        self.size = 0

    def insert(self, node, position=None):
        if not self.check_node(node):
            return False
        if not self.check_node(self.head):
            self.head = node
            return True

        temp = self.get_position(position)
        if not temp:
            return False
        if temp == self.head:
            return self.shift(node)

        node.next = temp.next
        temp.next = node
        self.size += 1
        return True

    def remove(self, node):
        if not self.check_node(node) or not self.check_node(self.head):
            return None

        temp = self.get_position(node)

        if not self.check_node(temp):
            return None
        elif node.data == self.head.data:
            self.head = self.head.next
        else:
            rm = temp.next
            temp.next = temp.next.next
            self.size -= 1
            return rm

    # Append the node to the end
    def append(self, node):
        return self.insert(node, None)

    # Append the node to the head of the list
    def shift(self, node):
        if not self.check_node(node):
            return False
        if self.is_empty():
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.size += 1
        return True

    # Remove the first node of the list
    def unshift(self):
        if not self.check_node(self.head):
            return None
        rm = self.head
        self.head = self.head.next
        self.size -= 1
        return rm

    # Remove last node
    def pop(self):
        if not self.check_node(self.head):
            return None
        temp = self.head
        prev = temp
        while temp.next:
            prev = temp
            temp = temp.next
        prev.next = None
        self.size -= 1
        return temp

    # get the length of the list
    def get_length(self):
        return self.size

    # with the index ,return the node. index's range(1,2,3....)
    def get_node(self, index):
        if not self.check_node(self.head):
            return None
        if index > self.size or index < 1:
            return None
        temp = self.head
        for i in range(index - 1):
            temp = temp.next
        return temp

    def index(self, node):
        if not self.check_node(self.head) or not self.check_node(node):
            return None
        temp = self.head
        index = 1
        while temp.next and temp.data != node.data:
            temp = temp.next
            index += 1
        if temp.data != node.data:
            return 0
        return index

    def is_empty(self):
        return self.size == 0

    def check_node(self, node):
        if not node:
            return False
        if not node.data:
            return False
        return True

    def get_position(self, node):
        """if not found the position or position is none,
        return the last pointer of head,
        otherwise return the position pointer"""
        temp = self.head
        if not self.check_node(node):
            while temp.next:
                temp = temp.next
            return temp
        if temp.data == node.data:
            return temp
        while temp.next and temp.next.data != node.data:
            temp = temp.next
        return temp.next and temp

    def print_item(self):
        temp = self.head
        while temp:
            print temp.data,
            temp = temp.next
        print ''

    def shuffle_list(self):
        import random
        self.b = [random.randint(1, 100) for i in xrange(20)]
        for i in self.b:
            self.shift(Node(i))

    # Test the function
    def test(self):
        self.remove(self.head)
        self.print_item()
        self.append(Node(200))
        self.print_item()
        self.remove(Node(self.b[10]))
        self.insert(Node(self.b[12]), Node(self.b[11]))
        self.print_item()
        self.pop()
        self.print_item()
        self.unshift()
        self.print_item()


if __name__ == "__main__":
    l = LinkList()
    l.shuffle_list()
    l.print_item()
    l.test()