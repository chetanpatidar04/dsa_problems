class node():
    def __init__(self,data):
        self.data = data
        self.next = None

class linke_list():
    def __init__(self):
        self.head = None
    
    def insert_data(self,data):
        if self.head is None:
            self.head = node(data)
            return        
        current = self.head
        while(current.next):
            current = current.next
        current.next = node(data)
    

    def travesal(self):
        if self.head is None:
            print("No element present in linked list")
            return None
        if self.head.next is None:
            print(self.head.data)
            return self.head
        current = self.head
        while(current):
            print(str(current.data) + " " ,end= "")
            current = current.next

#  Revererse without stack ========================================= 

    def reverse(self):
        if self.head == None:
            return
        current1 = self.head
        prev = None
        while(current1):
            next_node = current1.next
            current1.next = prev
            prev = current1
            current1 = next_node
            self.head = prev    
        return self.head


# Revererse with stack ========================================= 

    def reverse_with_stack(self):
        if self.head is None and self.head.next is None:
            return self.head
        current = self.head
        st = []
        new_head = None
        prev = None
        while(current):
            st.append(current)
            current = current.next
        for i in st:
            if new_head ==None:                
                prev = i
                new_head = prev
            prev.next = i
            prev = prev.next
            prev = i

# Revererse using recursions ========================================= 

    def reverse_using_recursion(self,head):
        if head is None or head.next is None:
            return head
        head = self.reverse_using_recursion(head)
        head.next.next = head.next
        head.next = None
        return head
        

    



linke_list = linke_list()
linke_list.insert_data(10)
linke_list.insert_data(20)
linke_list.insert_data(30)
linke_list.insert_data(40)
# linke_list.insert_data(50)
linke_list.travesal()
linke_list.reverse()
# linke_list.reverse_with_stack()
# linke_list.reverse_using_recursion(linke_list.head)
print("zb")
linke_list.travesal()