# Intersection in Y Shaped Lists

# You are given the heads of two non-empty singly linked lists, head1 and head2, that intersect at a certain point. return that node where these two linked lists intersect.

# Note: It is guaranteed that the intersected node always exists.

# Examples:

# Input: head1 : 4 -> 4 -> 4 -> 4 -> 4, head2 : 4 -> 4 -> 4
 
# Output: 4
# Explanation: From the above image, it is clearly seen that the common part is 4 -> 4 whose starting point is 4.

# Input: head1 : 4 -> 1 -> 8 -> 4 -> 5, head2 : 5 -> 6 -> 1 -> 8 -> 4 -> 5
 
# Output: 8
# Explanation: From the above image, it is clearly seen that the common part is 8 -> 4 -> 5 whose starting point is 8.


class node():
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.head = None
    
    # def insert_data(self,data):
    #     if self.head is None:
    #         self.head = node(data)
    #         return        
    #     current = self.head
    #     while(current.next):
    #         current = current.next
    #     current.next = node(data)
    

    def travesal(self,head=None):
        self.head = head
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

# =================================== Brute Force Approch =================================================
    def intersection_of_y_link_list(self,head1,head2):
        if self.head is None:
            return self.head
        if self.head.next is None:
            return self.head
        current1 = head1
        current2 = head2
        st = []
        while(current1):
            st.append(current1)
            current1 = current1.next

        while(current2):
            if current2 in st:
                print(current2.data)
                return current2.data
            current2 = current2.next
        
            


linked_list = linked_list()
shared = node(30)
shared.next = node(40)
shared.next.next = node(50)

head1 = node(10)
head1.next = node(20)
head1.next.next = shared

head2 = node(15)
head2.next = node(17)
head2.next = shared


linked_list.travesal(head1)
print("y list")
linked_list.travesal(head2)