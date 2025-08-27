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

# Brute Force Approch =================================================
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
                print("intersect at ==> ",current2.data)
                return current2.data
            current2 = current2.next
        print("No intersection")

#  Better solution =================================================
    def remove_prev_node(self,head,n):
        current = head
        new_head = None
        while(current):
            if n == 0:
                new_head = current
                del head
                return new_head
            n = n-1
            current = current.next

    def better_sol_intersection(self,head1,head2):
        if head1 is None:
            print("no head")
            return head1
        if head1.next == None:
            print("head data ",head1.data)
            return head1.data

        if head2 is None:
            print("no head")
            return head1
        if head2.next == None:
            return head1.data

        count_1 = 0
        count_2 = 0
        current = head1
        while(current):
            count_1 += 1
            current = current.next
        
        current2 = head2
        while(current2):
            count_2 += 1
            current2 = current2.next

        if count_1 > count_2:
            n = count_1 - count_2    
            head1 = self.remove_prev_node(head1,n)
        else:
            n = count_2 - count_1
            head2 = self.remove_prev_node(head2,n)

        current3 = head1
        current = head2
        while(current3):
            if current.next == current3.next:
                print("Intersection point ==> ",current3.next.data)
                return current3.next
            current = current.next
            current3 = current3.next    

#  Better solution =================================================
    def optimal_sol_intersection(self,head1,head2):
        temp1 = head1
        temp2 = head2

        while temp1 != temp2:
            if temp1 == temp2:
                print("optimal intersection point ==> ",temp1.data)
                return True
            temp1 = temp1.next if temp1 else head2
            temp2 = temp2.next if temp2 else head1
            
        if temp1:
            print("Optimal intersection point ==> ", temp1.data)
            return True
        else:
            print("No intersection point from optimal function")
            return False
        # print("No intersection point from optimal function")
        # return False





linked_list = linked_list()
shared = node(30)
shared.next = node(40)
shared.next.next = node(50)

head1 = node(10)
head1.next = node(20)
head1.next.next = shared

head2 = node(15)
head2.next = node(17)
head2.next.next = node(27)
head2.next.next.next = node(27)
head2.next.next.next.next = shared


linked_list.travesal(head1)
print("y list")
linked_list.travesal(head2)

print("intersection")
linked_list.intersection_of_y_link_list(head1,head2)
# linked_list.better_sol_intersection(head1,head2)
print("optimal solution")
linked_list.optimal_sol_intersection(head1,head2)
print("test")