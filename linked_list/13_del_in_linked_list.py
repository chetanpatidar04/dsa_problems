# Deletion at the Beginning of Linked List
# Deletion at Specific Position of Linked List
# Deletion at the End of Linked List


class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        if self.head is None:
            self.head = node(data)
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = node(data)

    def traverse(self):
        if not self.head:
            return None
        current = self.head
        while(current.next):
            print(f"{current.data} -> ", end="")
            current = current.next
        print(current.data)

############################################## Deletion at the Beginning of Linked List ############################################################################################
    def deletion_at_beginning(self):
        if self.head:
            current = self.head
            self.head = self.head.next
            del current
            print(self.head.data,"this is a new head")
            return True
        else:
            print("No nodes present in the list ")

    
############################################## Deletion at the End of Linked List ############################################################################################
    def deletion_at_the_end(self):
        if self.head:
            if self.head.next is None:
                self.head = None
                return True
            current = self.head
            prev_node = None
            while(current.next):
                prev_node = current
                print(prev_node.data,"vakue")
                current = current.next
                if current.next is None:
                    prev_node.next = None
                    del current
                    current = prev_node
        else:
            print("No nodes present in the list ")

# optimal_approch
    def deletion_at_the_end1(self):
        if self.head:
            if self.head.next is None:
                self.head = None
                return True
            second_last = self.head
            # prev_node = None
            while second_last.next.next:
                second_last = second_last.next
            second_last.next = None
        else:
            print("No nodes present in the list ")


############################################## Deletion at Specific Position of Linked List ############################################################################################
    def deletion_at_specific_position(self,pos):
        if not self.head:
            print("No node present in the list")
        if self.head.next is None and pos > 1:
            print("Node not present in list")
        
        current = self.head
        count = 1
        while(current.next):
            count += 1
            prev_node = current
            current = current.next          
            if count == pos:
                prev_node.next = current.next
                del current
                current = prev_node
            


linked_list = linked_list()
linked_list.insert(10)
linked_list.insert(20)
linked_list.insert(30)
linked_list.insert(40)
linked_list.traverse()
# linked_list.deletion_at_beginning()
# linked_list.deletion_at_the_end()
# linked_list.deletion_at_the_end1()
linked_list.deletion_at_specific_position(2)
print()
linked_list.traverse()