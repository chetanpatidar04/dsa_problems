# # Remove Nth node from end of the Linked List
# Given a linked list. The task is to remove the Nth node from the end of the linked list.

# Examples:  

# Input : LinkedList = 1 ->2 ->3 ->4 ->5 , N = 2
# Output : 1 ->2 ->3 ->5
# Explanation:  Linked list after deleting the 2nd node from last which is 4, is 1 ->2 ->3 ->5

 

# Input : LinkedList = 7 ->8 ->4 ->3 ->2 , N = 1 
# Output : 7 ->8 ->4 ->3  
# Explanation:  Linked list after deleting the 1st node from last which is 2, is 7 ->8 ->4 ->3  


class node():
    def __init__(self,data):
        self.data = data
        self.next = None
    
class link_list():
    def __init__(self):
        self.head = None
    
    def insert(self,data):
        if self.head is None:
            self.head = node(data)
            return self.head
        current = self.head
        while(current.next):
            current = current.next
        current.next = node(data)
        return self.head

    def trav(self):
        if self.head is None:
            return self.head
        if self.head.next is None:
            return self.head
        current = self.head
        while(current):
            print(" ==> ",str(current.data),end="")
            current = current.next
        return "true"


# ============================================ BruteForce approch ==========================================
    def remove_nth_node(self,nth):
        if self.head is None:
            return self.head
        if self.head.next is None:
            return self.head
        count = 0
        current = self.head
        while(current):
            count += 1
            current = current.next
        
        nth = count - nth
        count_nth = 0
        current1 = self.head
        while(current1):
            count_nth += 1
            if nth == count_nth:
                current1.next = current1.next.next
            current1 = current1.next
        return self.head

#============================================= Optimal approch ==========================================
    def remove_nth_node_optmial_sol(self,nth):
        if self.head == None:
            return 
        if self.head.next == None:
            return
        current = fast = self.head
        for i in range(nth-1):
            if fast.next is None:
                print("value of n is greater then nodes")
                return self.head
            fast = fast.next

        while(current):
            prev_node = current
            current = current.next
            fast = fast.next
            
            if fast is None:
                self.head = current
                break
            if fast.next is None:
                prev_node.next = current.next
                break

        return self.head   


linked_list = link_list()
head = linked_list.insert(10)
head = linked_list.insert(20)
head = linked_list.insert(30)
# head = linked_list.insert(40)
# head = linked_list.insert(50)
# head = linked_list.insert(60)
# head = linked_list.insert(70)
# head = linked_list.insert(80)
# head = linked_list.insert(90)
# head = linked_list.insert(100)

linked_list.trav()
print(" This is list after removed ")
# head = linked_list.remove_nth_node(5)
head = linked_list.remove_nth_node_optmial_sol(2)
print(" This is a optimal solution")
linked_list.trav()