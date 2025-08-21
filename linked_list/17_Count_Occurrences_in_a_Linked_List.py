# Given a singly linked list and a key, the task is to count the number of occurrences of the given key in the linked list.

# Example :

# Input : head: 1->2->1->2->1->3->1 , key = 1
# Output : 4

# Count-Occurrences-in-a-Linked-List_1
 
# Explanation: key equals 1 has 4 occurrences.

# Input : head: 1->2->1->2->1, key = 3
# Output : 0
# Explanation: key equals to 3 has 0 occurrences.



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


################################## Pairwise swap of linked list ################################################ 
    def pair_wise_swap_data(self):
        if self.head == None:
            print("No element present in the list")
            return
        if self.head.next == None:
            print(self.head.data)
            return
        current = self.head
        temp_count = 1                
        while (current.next):
            prev = current
            current = current.next      
            temp_count += 1
            if temp_count == 2:
                temp = current.data             
                current.data = prev.data
                prev.data = temp
                temp_count = 0

    def traverse(self,k):
        count = 0
        current = self.head
        while current:
            print(str(current.data) + " --> ", end="")
            if current.data == k:
                count += 1
            current = current.next
        print("this is the number of k present in the list ==> ",count)
          



linked_list = linked_list()
linked_list.head = node(1)
linked_list.head.next = node(2)
linked_list.head.next.next = node(1)
linked_list.head.next.next.next = node(3)
linked_list.head.next.next.next.next = node(1)
linked_list.head.next.next.next.next.next = node(4)
linked_list.head.next.next.next.next.next.next = node(1)

linked_list.traverse(1)