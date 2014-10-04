import linkedlist


class LinkedListInsertSort(linkedlist.LinkList):
    def __init__(self):
        linkedlist.LinkList.__init__(self)

    def insert_sort(self):
        if self.is_empty():
            return
        temp = self.head  # traverse the list
        node = temp.next
        while node and temp:
            if temp.data <= node.data:
                if not node.next:
                    return
                temp = temp.next
                node = temp.next
                continue
            # the current node data is less than prev node data
            # pop the node from the list
            temp.next = node.next
            #traverse the list to find proper place inserted into
            p = self.head
            if node.data < p.data:
                node.next = self.head
                self.head = node
            else:
                while p.next and p.next.data < node.data:
                    p = p.next
                # get the proper place
                node.next = p.next
                p.next = node
            node = temp.next

    def shell_sort(self):
        pass



if __name__ == "__main__":
    lis = LinkedListInsertSort()
    lis.shuffle_list()
    lis.print_item()
    lis.insert_sort()
    lis.print_item()