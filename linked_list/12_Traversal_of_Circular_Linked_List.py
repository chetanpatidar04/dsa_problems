class node():
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None

    def travesal(self):
        current = self.head
        while(current.next):
            print(str(current.data) + " --> ",end="")
            current = current.next
        print(current.data)


################################## Delete middle node from the list ################################################ 
    def traversal_circular_list(self):
        if self.head:
            if self.head.next == None:
                return True
        count = 1
        current = self.head
        while(current.next):
            print(str(current.data )+ "-->",end="")            
            current = current.next
            if current == self.head:
                return
            count += 1


          



linked_list = linked_list()
linked_list.head = node(10)
linked_list.head.next = node(20)
linked_list.head.next.next = node(30)
linked_list.head.next.next.next = node(40)
linked_list.head.next.next.next.next = node(50)
linked_list.head.next.next.next.next.next = linked_list.head
linked_list.traversal_circular_list()