class node:
    def __init__(self,data):
        self.data = data
        self.next = None


class linked_list:
    def __init__(self):
        self.head = None


############################################## Insert at the end of Linked List ############################################################################################

    def insert_at_end(self,data):
        if self.head is None:
            self.head = node(data)
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = node(data)

############################################## insert at the Beginning of Linked List ############################################################################################
    def insert_at_beginning(self,data):
        if not self.head:
            self.head = node(data)
            return True
        temp = self.head
        self.head = node(data)        
        self.head.next = temp


############################################## insert at the specific position of Linked List ############################################################################################
    def insert_at_specific_position(self,data,pos):
        if self.head:
            count = 1
            current = self.head
            while(current.next):
                count += 1
                temp = current.next
                if count == pos:          
                    new_node = node(data)
                    current.next = new_node
                    new_node.next = temp
                current = current.next


    def traverse(self):
        current = self.head
        while(current.next):
            print(str(current.data) + " --> ",end="")
            current = current.next
        print(current.data)



linked_list = linked_list()
linked_list.insert_at_end(10)
linked_list.insert_at_end(20)
linked_list.insert_at_end(30)
linked_list.insert_at_end(40)
linked_list.insert_at_beginning(50)
linked_list.insert_at_specific_position(60,3)

linked_list.traverse()